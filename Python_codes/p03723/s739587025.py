A,B,C=map(int,input().split())

if A==B==C and A%2==0:
    print(-1)
else:
    K=0
    while (A%2)+(B%2)+(C%2)==0:
        A,B,C=(B+C)//2,(C+A)//2,(A+B)//2
        K+=1
    print(K)
