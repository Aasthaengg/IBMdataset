N=int(input())
P=list(map(int, input().split()))

cnt=1

if N==1:
    print(1)
elif N==2:
    if P[1] < P[0]:
        print(2)
    else:
        print(1)
else:
    tmp = P[0]
    if P[1] <= P[0]:
        cnt +=1
    for i in range(2,N):
        tmp = min(P[i-1],tmp)
        if P[i] <= tmp:
            cnt+=1
    print(cnt)