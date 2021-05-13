l = list(map(int, input().split()))
k = int(input())
l = sorted(l, reverse=True)
for i in range(k):
  l[0] = l[0]*2
print(sum(l))