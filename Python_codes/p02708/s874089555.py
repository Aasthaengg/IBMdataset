n, k = map(int, input().split())

ans = 0

l = [0] * (n+2)
minv = 0
maxv = n

#print(l)
for i in range(1, n+2):
  #print(i)
  l[i] = maxv - minv + 1
  minv += i
  maxv += (n-i)

for i in range(k, n+2):
  ans = (ans + l[i]) % (10**9 + 7)

print(ans)