#!/usr/bin/env python3

O = input()
E = input()

for x,y in zip(O,E):
    print(x+y, end="")
if len(O) > len(E):
    print(O[-1])
else:
    print("")

