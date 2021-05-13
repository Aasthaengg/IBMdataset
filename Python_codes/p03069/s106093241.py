n = int(input())
s = input()
w = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
  b[i] = (0 if i==0 else b[i-1]) + (s[i]=='#')
  w[n-1-i] = (0 if i==0 else w[n-i]) + (s[n-1-i]=='.')
ans = 10000000000
for i in range(n+1):
  ans = min(ans, (0 if i==0 else b[i-1]) + (0 if i==n else w[i]))
print(ans)