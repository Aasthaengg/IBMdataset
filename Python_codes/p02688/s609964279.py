n, k = map(int, input().split())
L = []
for i in range(k):
  a = int(input())
  b = list(map(int, input().split()))
  for j in range(a):
    L.append(b[j])
l = list(set(L))
print(n - len(l))