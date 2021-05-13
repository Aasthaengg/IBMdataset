n = int(input())
a = list(map(int, input().split()))
while len(a) > 1:
  m = min(a)
  a = [a[i]%m for i in range(len(a)) if a[i]%m > 0]
  a.append(m)
print(m)
