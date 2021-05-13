import math

X = int(input())

for k in range(X,0,-1):
    for i in range(2,int(math.sqrt(k))+2,1):
        tmp = i
        tmp = tmp*i
        while tmp <= k:
            if tmp ==k:
                print(k)
                exit()
            tmp = tmp*i
print(1)