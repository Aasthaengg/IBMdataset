N=int(input())
L=[i**5 for i in range(150)]
for i in L:
    if N-i in L:
        if i-N>0:
            print(L.index(i),L.index(i-N))
        else:
            print(L.index(i),-1*L.index(N-i))
        break
    elif N+i in L:
        print(L.index(i+N),L.index(i))
        break