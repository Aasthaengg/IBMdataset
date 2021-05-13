def getDis(X,p):
    res = 0
    for x in X:
        res += (x-p)**2
    return res

n = int(input())
X = list(map(int,input().split()))

p = sum(X)//n

for i in range(n):
    d = getDis(X,p)
    if d>getDis(X,p+1):
        p+=1
    elif d>getDis(X,p-1):
        p-=1
    else:
        break

print(d)