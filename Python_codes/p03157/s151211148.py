def main():
    import sys
    input = sys.stdin.readline
    H, W = [int(x) for x in input().strip().split()]
    M = [0] * (H+2)
    M[0] = ['x'] * (W+2)
    M[-1] = ['x'] * (W+2)
    for h in range(H):
        M[h+1] = ['x'] + list(input().strip()) + ['x']

    dhdw = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ans = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            if M[i][j] == 'x':
                continue
            cnt = {'.':0, '#':0}
            q = [(i, j, M[i][j])]
            cnt[M[i][j]] = 1
            M[i][j] = 'x'
            while q:
                h, w, m = q.pop()
                # print(h, w)
                # for h_ in range(H+2):
                #     print(M[h_])
                for dh, dw in dhdw:
                    if M[h+dh][w+dw] != 'x' and m != M[h+dh][w+dw]:
                        cnt[M[h+dh][w+dw]] += 1
                        q.append((h+dh, w+dw, M[h+dh][w+dw]))
                        M[h+dh][w+dw] = 'x'
            # for h_ in range(H+2):
            #     print(M[h_])
            # print(cnt['.']*cnt['#'])
            ans += cnt['.']*cnt['#']
    
    print(ans)

if __name__ == '__main__':
    main()