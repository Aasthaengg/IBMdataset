n = int(input())
x = list(map(int , input().split()))
y = sorted(x)
ms = y[(n-1)//2]
ml = y[n//2]

for xi in x:
    if xi < ml:
        print(ml)
    else:
        print(ms)
