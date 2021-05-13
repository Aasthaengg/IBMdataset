a=input()
n=[]
for i in range(len(a)):
  if i%2==0:
    n.append(i)
ans=''
for i in n:
  ans=ans+a[i]
print(ans)