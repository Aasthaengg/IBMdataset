import sys
A,B,C=map(int,input().split())
cnt=0
A_old=B_old=C_old=0
for i in range(100000000):
    if A%2==1 or B%2==1 or C%2==1:
        print(cnt)
        sys.exit()
    elif  A==A_old and B==B_old and C==C_old:
        print(-1)
        sys.exit()

    A_old=A
    B_old=B
    C_old=C
    A=C_old/2+B_old/2
    B=A_old/2+C_old/2
    C=A_old/2+B_old/2
    cnt+=1
