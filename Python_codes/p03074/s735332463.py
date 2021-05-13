n, k = map(int, input().split())
s = str(input())
v = [0]
for i in range(len(s)-1):
  if s[i] != s[i+1]:
    v.append(i+1)
ans = 0
arr = v + [n] *(2*k+1)
for i, j in enumerate(v):
  if s[j] == "0":
    ans = max(ans, arr[i+2*k]-arr[i])
  else:
    ans = max(ans, arr[i + 2*k +1] -arr[i])
print(ans)