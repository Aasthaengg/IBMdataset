n,l=map(int,input().split())
a=[]
cnt=101
index=-1
for i in range(n):
  a.append(l+i)
for i in range(n):
  if cnt>=abs(0-a[i]):
    cnt=abs(0-a[i])
    index+=1
print(sum(a)-a[index])