import sys
inf = sys.maxsize

if __name__ == '__main__':
    h, w, k = map(int, sys.stdin.readline().strip().split())
    s = [[int(i) for i in sys.stdin.readline().strip()] for _ in range(h)]
    
    ans = inf
    for i in range(2 ** (h - 1)): #縦方向の割り方を全探索 O(512)
        hdiv = [1 if i & 2 ** j else 0 for j in range(h - 1)]
        hdiv.append(1)
        sh = sum(hdiv)
        tmpans = sh - 1
        partsum = [0 for _ in range(sh)]
        partsum_p = [0 for _ in range(sh)]
        j = 0
        for j in range(w): #O(10 ** 3)
            tmp = 0
            idx = 0
            flag = False
            for kk in range(h): #O(10)
                tmp += s[kk][j]
                if hdiv[kk]:
                    partsum_p[idx] = partsum[idx]
                    partsum[idx] += tmp
                    if partsum[idx] > k and not flag:
                        tmpans += 1
                        flag = True
                    tmp = 0
                    idx += 1
            if flag:
                partsum = [partsum[l] - partsum_p[l] for l in range(sh)]
                partsum_p = [0 for _ in range(sh)]
                for kk in range(sh):
                    if partsum[kk] > k:
                        tmpans = inf
                        break
        ans = min(ans, tmpans)
    print(ans)
