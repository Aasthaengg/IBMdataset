A,B,C=map(int,input().split())

Q=0
if A==B and B==C and C==A:
    if A%2==1 or B%2==1 or C%2==1:
        print(0)
    elif  A%2==0 or B%2==0 or C%2==0:
        print(-1)
else:
    for i in range(100):
        if A%2==1 or B%2==1 or C%2==1:
            print(Q)
            break
        else:
            A,B,C=(B+C)//2,(C+A)//2,(A+B)//2
            Q+=1

    
