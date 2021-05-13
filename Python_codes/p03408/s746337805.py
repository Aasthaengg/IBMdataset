n = (int)(input())
plus = [input() for i in range(n)]
m = (int)(input())
minus = [input() for i in range(m)]

maxi = 0
words = ""
for i in list(set(plus)):
  temp = plus.count(i) - minus.count(i)
  if maxi < temp:
    maxi = temp
    words = i
print(maxi)