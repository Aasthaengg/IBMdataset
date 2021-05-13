def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    ab = [0] * (N-1)
    num = [0] * N
    l = [[] for _ in range(N)]
    for n in range(N-1):
        a, b = [int(x)-1 for x in input().strip().split()]
        l[a].append(b)
        l[b].append(a)
    C = sorted([int(x) for x in input().strip().split()], reverse=True)
    ans = 0
    q = [0]
    i = 0
    while q:
        c = q.pop()
        num[c] = C[i]
        i += 1
        for n in l[c]:
            if num[n] == 0:
                q.append(n)

    print(sum(num)-C[0])
    print(*num)

if __name__ == '__main__':
    main()