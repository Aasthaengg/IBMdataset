import datetime

lst = input().split()

h1 = int(lst[0])
m1 = int(lst[1])
h2 = int(lst[2])
m2 = int(lst[3])
k = int(lst[4])

d = (60 * h2 + m2) - (60 * h1 + m1)

print(int(d - k))