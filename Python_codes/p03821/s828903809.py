n=int(input())
ans=0
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
for i in reversed(range(n)):
  if a[i][1] != 1 and a[i][0] != 0:
    a[i][0] += ans
    if a[i][0] % a[i][1] != 0:
      ans += a[i][1] - a[i][0] % a[i][1]
print(ans)