n,k = map(int, input().split())
c = [0] * n

for i in range(k):
  input()
  for a in list(map(int, input().split())):
    c[a-1] += 1
print(c.count(0))