n = int(input())
l = []
for i in range(n):
  a,b = map(int,input().split())
  l.append([a+b,a,b])
l1 = sorted(l)[::-1]
bit = 0
ans = 0
for i,j,k in l1:
  if bit==0:
    ans += j
    bit = 1
  else:
    ans -= k
    bit = 0
print(ans)