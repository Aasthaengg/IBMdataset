N=int(input())
a=N//11
ans=2*a
b=N-11*a
if 0<b<=6:
  ans+=1
elif 6<b<=10:
  ans+=2
print(ans)