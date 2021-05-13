n = int(input())
s = input()

w = [0]*n
e = [0]*n

for i in range(n):
  if s[i] == "W": w[i] += 1
  else: e[i] += 1
  if i != n-1:
    w[i+1] = w[i]
    e[i+1] = e[i]

ans = e[-1]-e[0]
for i in range(1,n):
  ans = min(ans, w[i-1] + e[-1]-e[i])
print(ans)