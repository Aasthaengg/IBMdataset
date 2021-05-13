n=int(input())
x=list(map(int,input().split()))

newx=sorted(x)

lower_med=newx[n//2-1]
higher_med=newx[n//2]

for i in range(n):
    if x[i]<=lower_med:
        print(higher_med)
    else:
        print(lower_med)