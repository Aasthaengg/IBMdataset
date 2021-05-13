N = int(input())
d = list(map(int, input().split()))
ans = 0
d.sort()
ans = d[int(N / 2)] - d[int(N / 2) - 1]
print(ans)
