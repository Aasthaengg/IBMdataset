x = int(input())
a = [input() for i in range(x)]
y = int(input())
b = [input() for h in range(y)]

count_max = 0
for j in a:
  if (a.count(j) - b.count(j)) > count_max:
    count_max = a.count(j) - b.count(j)
print(count_max)