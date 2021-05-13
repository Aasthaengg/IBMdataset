N=int(input())
s=0
for i in range(N):
  a,b=input().split()
  a=float(a)
  if b=="JPY":
    s+=a
  else:
    s+=(a*380000)
print(s)