A,B,C,D=map(int,input().split())
num = 0
while(A>=0 and C>=0):
    if A<= 100 and 0 <= B<= 100 and C<= 100 and 0 <= D<= 100:
        if num %2 == 0:
            C = C- B
            if C<=0:
                print("Yes")
                break
            num += 1
        elif num %2 !=0:
            A = A - D
            if A<=0:
                print("No")
                break
            num += 1
    else:
        break
