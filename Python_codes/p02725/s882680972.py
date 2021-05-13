k, n = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
lst.append(k + lst[0])

check = 0
for i in range(n):
  x = lst[i + 1] - lst[i]
  if (x > check):
    check = x

print(k - check)
