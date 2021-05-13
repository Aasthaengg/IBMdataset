# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

counter = 0

while True:
    even = True
    for i in a:
        if i % 2 != 0:
            even = False
            break
        else:
            even = True
    if even == False:
        break
    else:
        counter += 1
        a = list(map(lambda x: x / 2, a))

print(counter)