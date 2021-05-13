import math 

H = int(input())

def calc(h):
    if h == 1:
        return 1
    else:
        h = math.floor(h / 2)
        return calc(h) * 2 + 1

print(calc(H))