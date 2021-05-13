n= int(input())
s = [0]*n
t = [0]*n
u = [0]*n
v = {}
for i in range(n):
  a, b = input().split()
  s[i] = a
  t[i] = int(b)
x = input()

u[n-1]=0
v[s[n-1]]=0
for i in range(n-2,-1,-1):
  u[i] = t[i+1]+u[i+1]
  v[s[i]] = u[i]

print(v[x])