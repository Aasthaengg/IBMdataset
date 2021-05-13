[A,B] = list(map(int,input().split()))

s=A
i=1
while True:
    if B==1:
        print(0)
        break
    elif A==B:
        print(1)
        break

    elif s>=B:
        print(i)
        break
    s+=A-1
    i+=1

