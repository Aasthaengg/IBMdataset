X, N = map(int, input().split())
if N == 0:
  print(X)
  exit()
p = list(map(int, input().split()))

max_num = max(p)
lst = []
for i in range(max_num+2):
  if i not in p:
    lst.append(i)
tmp = float("inf")
for j in lst:
  if tmp > abs(X-j):
    tmp = abs(X-j)
    ans = j
print(ans)