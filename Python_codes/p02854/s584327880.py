n = (int)(input())
a = list(map(int, input().split(" ")))
total = sum(a)
temp = 0
for i in range(n):
  #print(a[i])
  temp += a[i]
  if temp >= total - temp:
    ko1 = abs(temp - (total - temp))
    temp -= a[i]
    ko2 = total - 2 * temp
    print(min(ko1, ko2))
    break