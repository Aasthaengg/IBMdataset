#!/usr/bin/env python3
x = int(input())
for i in range(50000):
    if int(i * 1.08) == x:
        print(i)
        quit()
print(':(')
