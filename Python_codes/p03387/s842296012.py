a,b,c = sorted(map(int,input().split()))
ans = 0
ans += (c-b)//2
b += (c-b)//2*2
ans += (c-a)//2
a += (c-a)//2*2
a,b,c = sorted([a,b,c])
if a==b and b!=c:
  print(ans+1)
elif a==b==c:
  print(ans)
elif b==c and b!=a:
  print(ans+2)