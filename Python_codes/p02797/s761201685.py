N,K,S=map(int,input().split())
l=[0]*N
if S==10**9:
    for i in range(N):
        if i<K:
            l[i]=str(S)
        else:
            l[i]=str(1)
else:
    for i in range(N):
        if i<K:
            l[i]=str(S)
        else:
            l[i]=str(10**9)
print(" ".join(l))