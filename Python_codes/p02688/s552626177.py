n, k = map(int, input().split())
a = []
for i in range(k):
  d = int(input())
  a[len(a):len(a)] = list(map(int, input().split()))
list(set(a))
ans = 0
for i in range(1, n+1):
  if i not in a:
    ans += 1
print(ans)