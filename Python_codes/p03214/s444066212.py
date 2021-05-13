n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
b = []
for i in range(n):
  b.append(abs(avg - a[i]))
print(b.index(min(b)))