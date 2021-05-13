n = int(input())
l = [int(input()) for _ in range(n)]
q = [0]*n
for i in range(n):
  q[l[i]-1] = i
a = 1
ans = 0
for i in range(1,n):
  if q[i]>q[i-1]:
    a += 1
  else:
    ans = max(ans,a)
    a = 1
print(n-max(ans,a))
