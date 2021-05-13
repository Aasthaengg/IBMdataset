n,k = map(int,input().split())

l = []
for _ in range(k):
  d = int(input())
  a = list(map(int,input().split()))
  l.extend(a)
  l = list(set(l))

print(n - len(l))