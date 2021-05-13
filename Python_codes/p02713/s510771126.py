K   = int(input())
Sum = 0
def mygcd(x,y):
    a = min(x,y)  # 最小値
    b = max(x,y)  # 最大値
    r = 2  # 余り
    while r != 0:
        r = b % a
        b = a
        a = r
    return b

for A in range(1,K+1):
    for B in range(1,K+1):
        AB = mygcd(A,B)
        if AB==1:
            Sum = Sum+K
        else:
            for C in range(1,K+1):
                Sum = Sum+mygcd(AB,C)
print(Sum)