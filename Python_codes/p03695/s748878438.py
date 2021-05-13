N=int(input())
A=list(map(int,input().split()))

rate=[0]*8
variety=0
special=0
for i in range(N):
    if A[i]<400:
        if rate[0]==0:
            variety+=1
        rate[0]+=1
    elif A[i]<800:
        if rate[1]==0:
            variety+=1
        rate[1]+=1
    elif A[i]<1200:
        if rate[2]==0:
            variety+=1
        rate[2]+=1
    elif A[i]<1600:
        if rate[3]==0:
            variety+=1
        rate[3]+=1
    elif A[i]<2000:
        if rate[4]==0:
            variety+=1
        rate[4]+=1
    elif A[i]<2400:
        if rate[5]==0:
            variety+=1
        rate[5]+=1
    elif A[i]<2800:
        if rate[6]==0:
            variety+=1
        rate[6]+=1
    elif A[i]<3200:
        if rate[7]==0:
            variety+=1
        rate[7]+=1
    else:
        special+=1

if special==0:
    print(variety,variety)
elif variety==0:
    print(1,special)
else:
    print(variety,variety+special)