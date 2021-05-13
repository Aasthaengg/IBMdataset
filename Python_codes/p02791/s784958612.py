N = int(input())
d = list(map(int, input().split()))

c = 1
a = d[0]

for i in range(1,N):
  if d[i] <= a:
    c += 1
    a = d[i]

print(c)