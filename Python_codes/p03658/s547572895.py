N, K = map(int, input().split())
a = list(map(int, input().split()))
max = 0
a.sort(reverse=True)
for i in a[0:K]:
  max += i
print(max)