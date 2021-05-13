def f(a):
  if a%2==0:
    return a//2
  else:
    return 3*a+1

s=int(input())
cnt=1
while s!=4 and s!=2 and s!=1:
  cnt+=1
  s=f(s)
print(cnt+3)