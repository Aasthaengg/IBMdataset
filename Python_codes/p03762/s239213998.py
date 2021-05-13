Mod = 10**9+7
n = [0,0]
n[0],n[1] = map(int,input().split())
a = [0,0]
for j in range(2):
  x = list(map(int,input().split()))
  s = 0
  for i in range(n[j]):
    s = (s+x[i]*(2*i+1-n[j]))%Mod
  a[j] = s
print((a[0]*a[1])%Mod)