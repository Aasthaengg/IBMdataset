a,b,k=map(int, input().split())
alist=[]
cnt=0
for i in range(1,101):
  if a%i==0 and b%i==0:
    alist.append(i)
    cnt+=1
print(alist[cnt-k])