n = int(input())
InputNum = input().split()
a = []
for x in range(n):
    a.append(int(InputNum[x]))
a.sort()
min = a[0]
a.reverse()
max = a[0]
sum = 0
for y in range(n):
    sum += int(a[y])

print(min,max,sum)