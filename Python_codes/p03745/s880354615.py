import math
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
flag = "Init"
ans = 0
for i in range(1, n):
    if flag == "Init":
        if a[i - 1] == a[i]:
            pass
        elif a[i - 1] > a[i]:
            flag = "-"
        else:
            flag = "+"
    elif flag == "-":
        if a[i - 1] < a[i]:
            ans += 1
            flag = "Init"
    else:
        if a[i - 1] > a[i]:
            ans += 1
            flag = "Init"
print(ans + 1)