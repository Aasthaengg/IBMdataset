n=int(input())
ans=0.0
for i in range(n):
  x,u=input().split()
  ans+=(float(x) if u=="JPY" else float(x)*380000.0)
print(ans)