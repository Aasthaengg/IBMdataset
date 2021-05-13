N=int(input())
ans=0
for i in range(N):
   A,B=list(input().split())
   if B=="JPY":
      ans+=int(A)
   else:
      ans+=float(A)*380000
print(ans)
