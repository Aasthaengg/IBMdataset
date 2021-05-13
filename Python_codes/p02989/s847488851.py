n = int(input())
d = list(map(int, input().split()))
ans = 0
d.sort()
print(max(0, d[n//2]-d[n//2-1]))
