N=int(input())
E={"*":0}
for _ in range(N):
    S=input()
    if S in E:
        E[S]+=1
    else:
        E[S]=1

M=int(input())
for _ in range(M):
    S=input()
    if S in E:
        E[S]-=1
    else:
        E[S]=-1

print(max(E.values()))
