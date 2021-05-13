n = int(input())
lev = [int(i) for i in input().split()]

lev_s = sorted(lev)
ans = 0

if lev_s[n//2] == lev_s[n//2 - 1]:
  print(0)
else:
  print(abs(lev_s[n//2] - lev_s[n//2 - 1]))