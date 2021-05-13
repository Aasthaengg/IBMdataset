# -*- coding: utf-8 -*-
for i in range(int(input())):
    values = sorted(map(lambda x: int(x)**2, input().split(' ')))
    if values[2] == values[1] + values[0]:
        print("YES")
    else:
        print("NO")

