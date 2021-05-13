n = int(input())
s = input()
t1 = [0]*n
t2 = [0]*n
for i in range(1, n):
  t1[i] = t1[i-1] + (s[i-1] == 'W')
  t2[n-i-1] = t2[n-i] + (s[n-i] == 'E')
ans = n
for i in range(n):
  ans = min(ans, t1[i] + t2[i])
print(ans)