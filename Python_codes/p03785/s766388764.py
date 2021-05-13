N,C,K=map(int,input().split())
T=[0]*N
for i in range(N):
    T[i]=int(input())
T.sort()

First_passengering=False
X=0
for k in range(N):
    t=T[k]

    if not First_passengering:
        X+=1
        First_passengering=True
        Dead_line=t+K
        Remain=C-1
    else:
        Remain-=1

    try:
        if T[k+1]>Dead_line:
            First_passengering=False
    except:
        pass

    if Remain==0:
        First_passengering=False

print(X)