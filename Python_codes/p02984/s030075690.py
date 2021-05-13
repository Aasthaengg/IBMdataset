n = int(input())
a = list(map(int,input().split()))
k = sum(a)
c = 0
ans = [0]*n
for i in range(n//2):
  c += a[i*2+1]
one = k - 2*c
ans[0] = one
for j in range(1,n):
  ans[j] = (a[j-1] - ans[j-1]//2)*2
for ji in ans:
  print(ji,end=' ')