n, k = map(int,input().split())
l = []
for i in range(1,n+1):
  l.append(i)
for i in range(k):
  d = int(input())
  a = list(map(int,input().split()))
  for j in range(d):
    if a[j] in l:
      l.remove(a[j])
print(len(l))