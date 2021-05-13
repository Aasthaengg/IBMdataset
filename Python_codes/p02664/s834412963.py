t=list(map(str,input().split()))
T=[]
for i in range(len(t[0])):
    T.append(t[0][i])
for i in range(len(T)):
    if T[i]=='?':
        T[i]='D'
U="".join(T)
print(U)