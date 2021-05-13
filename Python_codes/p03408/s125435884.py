l={}
N=int(input())
for i in range(N):
    a=input()
    if a in l:
        l[a]+=1
    else:
        l[a]=1
M=int(input())
for j in range(M):
    b=input()
    if b in l:
        l[b]-=1

if max(l.values())<=0:
    print(0)
else:
    print(max(l.values()))
