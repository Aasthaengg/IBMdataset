n = int(input())
s = str(input())

#n = 12
#s = 'WEWEWEEEWWWE'

w = [0] * (n+1)
e = [0] * (n+1)

for i in range(n):
  w[i+1] = w[i]
  e[i+1] = e[i]
  if s[i] == 'W':
    w[i+1] += 1
  else :
    e[i+1] += 1

#  w  ([0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6],
#  e   [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6])

ans = n
for i in range(1,n+1):
  # 自分より左にいるwの数 w[i-1]
  # 自分より右にいるeの数 e[n] - e[i]
  ans = min(ans, w[i-1] + (e[n] - e[i]) )

print(ans)

