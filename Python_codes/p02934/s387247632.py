n = int(input())
a = list(map(int, input().split()))
A = []
for i in range(n):
  s = 1 / a[i]
  A.append(s)

print(1/(sum(A)))