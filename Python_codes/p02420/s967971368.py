c=input()
while c!='-':
    #print(c)
    C=list(c)
    #print(C)
    l=int(input())
    #print(l)
    for i in range(l):
        n=int(input())
        for j in range(n):
            C.append(C[j])
        del C[0:n]
        #print(C)
    print(''.join(C))
    c=input()
