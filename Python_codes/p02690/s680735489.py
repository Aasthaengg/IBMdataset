import os

x = int(input())

for a in range(-118,120):
    for b in range(-119,119):
        if a**5-b**5==x:
            print("{} {}".format(a,b))
            exit()
