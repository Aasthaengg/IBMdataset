n = int(input())
a = list(map(int, input().split()))
mean = sum(a)/n
for i in range(n):
  a[i] = abs(a[i] - mean)
print(a.index(min(a)))