n=int(input())
hoge=100
ans=0
while hoge<n:
  hoge+=hoge//100
  ans+=1
  
print(ans)