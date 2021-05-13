#!/usr/bin/env python3
def collatz(number):
    if number % 2 == 0:
        return number // 2  # 整数の商
    else:  # elseで良い
        return 3 * number + 1  # // intは不要では？


number = int(input())
if number == 1:
    print(4)
    quit()
a = [number]
while True:
    number = collatz(number)
    a += [number]

    if number == 1:
        break
if 4 in a:
    print(a.index(4)+4)
elif 2 in a:
    print(a.index(2)+4)
else:
    print(a.index(1)+4)
