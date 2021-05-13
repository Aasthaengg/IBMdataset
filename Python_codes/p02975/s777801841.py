from sys import stdin
from itertools import groupby
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
li.sort()
lin = []
for key, value in groupby(li):
    lin.append((key,len(list(value))))
if len(lin) == 1 and lin[0][1] == n and lin[0][0] == 0:
    print("Yes")
elif n%3 != 0:
    print("No")
elif len(lin) == 2:
    lin.sort()
    if lin[0][1] == n//3:
        print("Yes")
    else:
        print("No")
elif len(lin) == 3:
    if lin[0][1] == lin[1][1] == lin[2][1] and lin[0][0]^lin[1][0]^lin[2][0] == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")