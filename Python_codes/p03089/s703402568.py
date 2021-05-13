import collections
def main():
    N = int(input())
    B = [0] + [int(_) for _ in input().split()]

    for i in range(1, N+1):
        if i < B[i]:
            print(-1)
            return
    dic = collections.defaultdict(int)
    for i in range(1, N+1):
        x = B[i]
        c = 0
        for j in range(i+1, N+1):
            if B[j] <= x:
                x += 1
                c += 1
        dic[B[i]+c] = B[i]
    out = [dic[key] for key in sorted(dic.keys())]
    print(*out, sep = '\n')
    return

if __name__ == '__main__':
    main()
