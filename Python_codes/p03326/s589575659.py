def main():
    from sys import stdin
    input = stdin.buffer.readline

    n, m = map(int, input().split())
    x, y, z = [0] * n, [0] * n, [0] * n
    for ind in range(n):
        i, j, k = map(int, input().split())
        x[ind] = i
        y[ind] = j
        z[ind] = k

    from itertools import product
    ans = 0
    for i, j, k in product([True, False], repeat=3):
        l = [0] * n
        if i:
            for ind in range(n):
                l[ind] += x[ind]
        else:
            for ind in range(n):
                l[ind] -= x[ind]
        if j:
            for ind in range(n):
                l[ind] += y[ind]
        else:
            for ind in range(n):
                l[ind] -= y[ind]
        if k:
            for ind in range(n):
                l[ind] += z[ind]
        else:
            for ind in range(n):
                l[ind] -= z[ind]

        l.sort(reverse=True)
        candidate = sum(l[:m])
        if ans < candidate:
            ans = candidate
    
    print(ans)

main()