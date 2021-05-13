N =input()
n=int(N)
k = len(N)
J = "9"*(k-1)
if N[1::]==J:
    print(int(N[0])+9*(k-1))
else:
    print(int(N[0])-1+9*(k-1))

