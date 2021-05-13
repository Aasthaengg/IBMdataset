n = int(input())
m = list(map(int,input().split()))
k = 0
for i in m:
  k ^= i
l = []
for i in m:
  l.append(k ^ i)
print(*l)