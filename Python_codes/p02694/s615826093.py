x=int(input())
ans=0
money=100
while money<x:
  ans+=1
  money=money+money//100
print(ans)
