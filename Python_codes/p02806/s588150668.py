N=int(input())
s,t=list(),list()
for i in range(N):
  a,b=input().split()
  s.append(a)
  t.append(int(b))
X=input()
m = N
result = 0
for n in range(N):
  if X == s[n]:
    m = n
  if m < n:
    result += t[n]
print(result)