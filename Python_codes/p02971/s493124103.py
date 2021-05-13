n=int(input())
A=[int(input()) for i in range(n)]
B=sorted(A,reverse=True)
amax=B[0]
asec=B[1]
for a in A:
    if a==B[0]:
        print(asec)
    else:
        print(amax)