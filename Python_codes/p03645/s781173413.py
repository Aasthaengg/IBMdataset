N,M=list(map(int, input().split()))
S=set()
D=[]
for i in range(M):
    l=list(map(int, input().split()))
    if l[0]==1:
        S.add(l[1])
    else:
        D.append(l)
# print(S)
# print(D)
D.sort()
L=len(D)
for i in range(L):
    if D[i][1]==N and D[i][0] in S:
        print('POSSIBLE')
        exit()
else:
    print('IMPOSSIBLE')