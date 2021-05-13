n = int(input())
a = list(map(int, input().split()))
t = 0
for i in range(1, n-1):
  if sorted(a[i-1:i+2]).index(a[i]) == 1:
    t += 1
print(t)