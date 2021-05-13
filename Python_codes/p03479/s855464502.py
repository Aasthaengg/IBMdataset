import fractions
#import math

def lcm(x, y):
    #return (x * y) // math.gcd(x, y)
    return (x * y) // fractions.gcd(x, y)

x, y = map(int,input().split())

if y < 2*x: #長さが1になる場合
    print(1)
    exit()

li = [x, 2*x]
i = 0

while True:
    x = lcm(li[i], li[i+1])*2
    if x <= y:
        li.append(x)
        i += 1
    else:
        print(len(li))
        exit()