n, k , s = map(int, input().split())
ans = []
for i in range(k):
  ans.append(str(s))
for i in range(n-k):
  if s == 1:
    s = 10
  ans.append(str(s//2+1))
print(" ".join(ans))