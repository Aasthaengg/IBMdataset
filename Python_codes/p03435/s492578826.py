A = list(map(int, input().split()))
A += list(map(int, input().split()))
A += list(map(int, input().split()))
flag=0
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1=A[6]-a1
            b2=A[7]-a1
            b3=A[8]-a1
            if b1<0 or b2<0 or b3<0:
                break
            if a3+b1==A[0] and a3+b2==A[1] and a3+b3==A[2] and a2+b1==A[3] and a2+b2==A[4] and a2+b3==A[5]:
                flag=1
print("Yes" if flag==1 else "No")
