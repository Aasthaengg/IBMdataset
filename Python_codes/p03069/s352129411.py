n = int(input())
s = input()

l = [0 for i in range(n)]
r = [0 for i in range(n)]
for i in range(1,n):
  rev = -(i+1)
  l[i] = l[i-1] + 1 if s[i-1] == "#" else l[i-1]
  r[rev] = r[rev+1] + 1 if s[rev+1] == "." else r[rev+1]

ans = 1e+9
for i in range(n):
  ans = min(ans, l[i] + r[i])
print(ans)