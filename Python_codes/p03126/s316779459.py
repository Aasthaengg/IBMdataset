n, m = [int(x) for x in input().split()]
a = {i : 0 for i in range(1, m+1)}

for _ in range(n):
  k, *likes = [int(x) for x in input().split()]
  for l in likes:
    a[l] += 1

result = len(list(filter(lambda x : x == n, a.values())))
print(result)