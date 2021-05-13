n,k=map(int,input().split())
s=input()
a=[]
cnt=0
flag=s[0]
for i in range(1,n):
  if flag==s[i]:cnt+=1
  else:
    flag=s[i]
    a+=[cnt]
    cnt=0
a+=[cnt]
print(min(sum(a)+2*k,n-1))