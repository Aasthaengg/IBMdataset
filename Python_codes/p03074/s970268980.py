n, k = map(int, input().split())
s = "#" + input()
B = []
L = []
for i in range(n):
  if s[i] != s[i+1]:
    B.append(int(s[i+1]))
    L.append(i+1)
ans = 0
for j, b in enumerate(B):
  if b == 0:
    if j+2*k >= len(L):
      ans = max(ans, n+1 - L[j])
    else:
      ans = max(ans, L[j+2*k] - L[j])
  else:
    if j+2*k+1 >= len(L):
      ans = max(ans, n+1 - L[j])
    else:
      ans = max(ans, L[j+2*k+1] - L[j])
print(ans)