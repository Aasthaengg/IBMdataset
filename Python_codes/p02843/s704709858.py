x=int(input())

h=x//100
t=x%100
ans=1
if h*5<t:
  ans=0
print(ans)