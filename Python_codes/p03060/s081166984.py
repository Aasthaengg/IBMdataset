n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

z = []
for i in range(n):
  z.append(v[i]-c[i])
#print(z)
ans = 0
for i in z:
  if i >= 0:
    ans += i

print(ans)