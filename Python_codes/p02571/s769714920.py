s = input()
t = input()
a = len(s)
b = len(t)
ans = 2000
for i in range(a-b+1):
  k = 0
  for j in range(b):
    if s[i+j] != t[j]:
      k += 1
  ans = min(ans,k)
print(ans)