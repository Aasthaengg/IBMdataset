n = int(input())
a = list(map(int, input().split()))

a.append(0)

money = 1000
h = a[0]
l = a[0]

for i in a:
  if h < i:
    h = i
  elif h > i and h > l:
    money = money//l * h + money%l
    h = l = i
  elif h > i:
    h = i
  if l > i:
    l = i

print(money)