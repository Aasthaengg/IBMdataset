#!/usr//bin/env python3.6
# -coding:UTF-8-

ab=input().split()
a=int(ab[0])
b=int(ab[1])
list=[a+b,a-b,a*b]
list.sort()
print(list[2])