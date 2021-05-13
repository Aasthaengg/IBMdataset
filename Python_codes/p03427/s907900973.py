N = input().strip()
k = len(N)
if k==1:
    print(int(N))
else:
    if N[1:]=="9"*(k-1):
        print(int(N[0])+9*(k-1))
    else:
        print(int(N[0])-1+9*(k-1))