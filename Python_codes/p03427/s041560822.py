N = input()
if len(N)==1:
    print(int(N))
else:
    if all(N[i]=='9' for i in range(1,len(N))):
        print(sum(int(i) for i in N))
    else:
        print(int(N[0])-1 + 9*(len(N)-1))