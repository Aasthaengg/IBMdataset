A,B,C = map(int,input().split())
count=0
if A==B==C and A%2==0 :
    print(-1)
elif A==B==C and A%2==1 :
    print(0)
else :
    while True :
        if A%2 != 0 or B%2 != 0 or C%2 != 0 :
            print(count)
            break
        elif A==B and B==C :
            print(-1)
            break
        else :
            count += 1
            dA=A
            dB=B
            dC=C
            A=dB/2+dC/2
            B=dA/2+dC/2
            C=dA/2+dB/2