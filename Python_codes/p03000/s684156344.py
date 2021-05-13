N,X = map(int,input().split())
L = list(map(int,input().split()))

curCoord = 0
n = 1

while (curCoord<=X):
    n = n+1
    
    if (n>N+1):
        break
    else:
        curCoord = curCoord+L[n-2]

print(n-1)