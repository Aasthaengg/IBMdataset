def money(n):
  if n==1:
    return 300000
  elif n==2:
    return 200000
  elif n==3:
    return 100000
  else:
    return 0

a,b=map(int,input().split())

ans=money(a)+money(b)+400000 if a==b==1 else money(a)+money(b)
print(ans)