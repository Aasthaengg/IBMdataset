N=int(input())
*X,=map(int,input().split())
Y=sorted(X)

mr=Y[N//2]
ml=Y[N//2-1]

for x in X:
    if mr<=x:
        print(ml)
    else:
        print(mr)