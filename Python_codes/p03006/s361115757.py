from itertools import combinations
N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
if N==1:
    print(1)
else:
    C = {}
    for z in combinations(X,2):
        x1,x2 = z
        a = x1[0]-x2[0]
        b = x1[1]-x2[1]
        if a>=0 and b>=0:
            if (a,b) not in C:
                C[(a,b)] = 0
            C[(a,b)] += 1
        elif a>0 and b<0:
            if (a,b) not in C:
                C[(a,b)] = 0
            C[(a,b)] += 1
        elif a==0 and b<0:
            if (a,-b) not in C:
                C[(a,-b)] = 0
            C[(a,-b)] += 1
        elif a<0 and b>0:
            if (-a,-b) not in C:
                C[(-a,-b)] = 0
            C[(-a,-b)] += 1
        elif a<0 and b==0:
            if (-a,b) not in C:
                C[(-a,b)] = 0
            C[(-a,b)] += 1
        elif a<0 and b<0:
            if (-a,-b) not in C:
                C[(-a,-b)] = 0
            C[(-a,-b)] += 1
    C = sorted(list(C.items()),key=lambda x:x[1],reverse=True)
    k = C[0][1]
    print(N-k)