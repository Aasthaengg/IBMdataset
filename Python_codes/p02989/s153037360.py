n = int(input())
d = list(map(int,input().split()))
d.sort()
if d[int(n/2)] == d[int(n/2)-1]:
  ans = 0
else:
  ans = d[int(n/2)] - d[int(n/2)-1]
print(ans)