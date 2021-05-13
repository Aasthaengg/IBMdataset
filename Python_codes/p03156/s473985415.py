n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

first = 0
second = 0
third = 0
ans = []

for i in range(len(p)):
  if p[i] <= a:
    first += 1
  elif p[i] >= a+1 and p[i] <= b:
    second += 1
  elif p[i] >= b+1:
    third += 1

ans.append(first)
ans.append(second)
ans.append(third)

print(min(ans))