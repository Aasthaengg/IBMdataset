n, k = map(int, input().split())
l = list(map(int, input().split()))
L = sorted(l, reverse=True)
a = 0
for i in range(k):
  a = a + L[i]
print(a)