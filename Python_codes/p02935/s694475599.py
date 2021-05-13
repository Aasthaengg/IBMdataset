n=int(input())
v=list(map(int,input().split()))
ans=0
while len(v) != 1:
  a=min(v)
  v.remove(a)
  b=min(v)
  v.remove(b)
  ans=(a+b)/2
  v.append(ans)


print(ans)