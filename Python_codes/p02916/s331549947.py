n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

satisfy = 0

for i in range(n):
  satisfy += b[a[i] - 1]
  if i == n-1:
    break
  if a[i+1] == a[i] + 1:
    satisfy += c[a[i] - 1]

print(satisfy)
