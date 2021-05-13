n = int(input())
s = list(input())

ans = 0
for i in range(1,n-1):
  w1,w2 = s[:i],s[i:]
  ans = max(ans, len(set(w1)&set(w2)))
print(ans)