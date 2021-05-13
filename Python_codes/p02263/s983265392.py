A=input().split()
B=[]
for i in A:
    if i.isdigit():
        B.append(int(i))
    else:
        if i=="+":
            B[-1]=B[-2]+B[-1]
            del B[-2]
        elif i=="-":
            B[-1]=B[-2]-B[-1]
            del B[-2]
        elif i=="*":
            B[-1]=B[-2]*B[-1]
            del B[-2]
print(B[0])