n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(n):
  c=0
  while l[i]%2==0:
    l[i]=l[i]//2
    c+=1
  cnt+=c
print(cnt)
