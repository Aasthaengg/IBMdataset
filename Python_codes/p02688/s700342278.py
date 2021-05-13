n, k = map(int,input().split())
lst = [0 for i in range(n)]
for i in range(k):
  x = int(input())
  lst2 = list(map(int,input().split()))
  for j in range(x):
    if (lst[lst2[j] - 1] == 0):
      lst[lst2[j] - 1] = 1
ans = 0
for i in range(n):
  if (lst[i] == 0):
    ans = ans + 1
print(ans)
