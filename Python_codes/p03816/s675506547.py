from sys import stdin
from itertools import groupby

n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
li.sort()

lin = []

for key, value in groupby(li):
    lin.append([key,len(list(value))])

point = 0

for i in lin:
    if i[1] >= 3:
        while True:
            if i[1] < 3:
                break
            i[1] -= 2

iti = 0
ni = 0

for i in lin:
    if i[1] == 1:
        iti += 1
    else:
        ni += 1

if ni%2 == 0:
    print(iti+ni)
else:
    print(iti+ni-1)