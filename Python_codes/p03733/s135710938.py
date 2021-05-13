n,T=[int(_) for _ in input().split()]
t=[int(_) for _ in input().split()]
ans=0
for i in range(n-1):
  ans += min(t[i+1]-t[i],T)
  
print(ans+T)