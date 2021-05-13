n=int(input())
a=[int(x) for x in input().split()]
cnt=0
for i in range(n):
  while a[i]%2==0:
    cnt+=1
    a[i]//=2
print(cnt)
