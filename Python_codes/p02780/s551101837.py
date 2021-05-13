n, k = map(int, input().split())
p = list(map(int, input().split()))
expected_value = [sum(p[:k])]

for i in range(n - k):
  expected_value.append(expected_value[-1]-p[i]+p[i+k])
print((max(expected_value)+k)/2)