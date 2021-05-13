import sys
def I(): return int(sys.stdin.readline().rstrip())


X = I()

for i in range(X,1000000):
    for j in range(2,int(i**.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
        break
