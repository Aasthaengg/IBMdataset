import math
def main(a,b,c):
    temp = math.floor(b/a)
    return temp if temp <= c else c

a,b,c = map(int, input().split())
print(main(a,b,c))