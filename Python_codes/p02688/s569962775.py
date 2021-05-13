n, k=map(int, input().split())

a = []
for i in range(k):
  int(input())
  x = list(map(int, input().split()))
  b = a + x
  a = list(set(b))
print(n - len(a))