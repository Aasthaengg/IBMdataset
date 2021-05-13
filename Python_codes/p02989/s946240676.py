N = int(input())
d = list(map(int, input().split()))

d.sort()

n = int(N / 2)

ans = d[n] - d[n - 1]

print(ans)