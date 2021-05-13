n, k = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * n
for i in a:
  c[i - 1] += 1
print(sum(sorted(c, reverse=True)[k:]))
