n=int(input())
data=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans=[]
res=n
while res>0:
  m=res%26
  res=(res-1)//26
  if m==0:
    ans.append('z')
  else:
    ans.append(data[m-1])
ans.reverse()
print(*ans,sep='')