n = int(input())
counter = dict()
for i in range(n):
  s = ''.join(sorted(input()))
  if not s in counter:
    counter[s] = 0
  counter[s] += 1
print(sum(x * (x-1) // 2 for x in counter.values()))