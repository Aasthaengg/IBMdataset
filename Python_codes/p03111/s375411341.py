def main():
    from itertools import product

    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    ans = 3000
    for prod in product([0, 1, 2, 3], repeat=N):
        t = [[] for _ in range(3)]
        for i, x in enumerate(prod):
            if x == 3: continue
            t[x].append(i)
        if (not t[0]) or (not t[1]) or (not t[2]): continue

        cost = sum(len(t[i]) - 1 for i in range(3)) * 10
        a = sum(L[i] for i in t[0])
        b = sum(L[i] for i in t[1])
        c = sum(L[i] for i in t[2])
        cost += abs(A - a) + abs(B - b) + abs(C - c)
        if ans > cost:
            ans = cost

    print(ans)


if __name__ == '__main__':
    main()
