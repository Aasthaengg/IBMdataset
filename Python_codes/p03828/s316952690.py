from sys import stdin

N= int(stdin.readline().rstrip())
values = list(range(1,N+1))

c = 1000000007

count = dict()
for i, v in enumerate(values):
  if v > 1:
    count[v] = count.get(v, 0) + 1
    for j in range(i+1, N):
      if (values[j] % v == 0):
          values[j] /= v
          count[v] += 1

result = 1
for v in count.values():
  result = (result * (v + 1)) % c
print(result)