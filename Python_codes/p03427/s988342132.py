N=input()

k=len(N)
A='9'*(k-1)

if N[0]==1:
    if N[1:]==A:
        print(k*9-8)
    else:
        print((k-1)*9)

else:
    if N[1:]==A:
        print(int(N[0])+(k-1)*9)
    else:
        print(int(N[0])+(k-1)*9-1)