X, N = map(int, input().split())
if N: p = list(map(int, input().split()))
else: print(X); exit()
length = 10**4+2
ans = -1
for i in range(-1,103):
  if length > abs(X - i) and i not in p:
    length = abs(X - i)
    ans = i
print(ans)