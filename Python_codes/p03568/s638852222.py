n = int(input())
a = list(map(int, input().split()))


ans = 0


def solve(i, l):
    global ans

    if len(l) == n:
        total = 1
        for k in l:
            total *= k
        if total % 2 == 0:
            ans += 1
        return

    for j in range(-1, 2):
        l.append(a[i] + j)
        solve(i + 1, l)
        l.pop()


solve(0, [])
print(ans)
