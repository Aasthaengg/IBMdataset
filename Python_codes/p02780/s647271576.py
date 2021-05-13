n,k=map(int,input().split())
p=list(map(int,input().split()))

def kitai(n):
  result = 0
  for i in range(1,n+1):
    result += i
  return result/n

s=[0]*(n+1)
for i in range(n):
  s[i+1] = s[i] + p[i]

resi = 0
tmp = 0
for i in range(n-k+1):
  if s[i+k]-s[i] > tmp:
    resi = i
    tmp = s[i+k]-s[i]

result = 0
for i in range(resi,k+resi):
  result += kitai(p[i])
print(result)