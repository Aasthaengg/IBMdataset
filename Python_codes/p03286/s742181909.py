n=int(input())
ans=""
while n!=0:
  ans=str(n%(2))+ans
  n=-(n//(2))
print(0 if ans =="" else ans)
