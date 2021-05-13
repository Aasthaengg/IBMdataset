#coding: utf-8
import sys
data = list(i for i in input().split())

for i in range(len(data)-1):
    if (data[i][-1] == data[i + 1][0]):
        continue
    else:
        print("NO")
        sys.exit()
else:
    print("YES")