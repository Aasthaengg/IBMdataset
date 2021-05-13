N=int(input())
D=list(map(int, input().split()))
M=int(input())
T=list(map(int, input().split()))
import bisect
D=sorted(D)
T=sorted(T)
idx=0
for i in range(M):
    t=T[i]
    while D[idx]<t:
        idx+=1
    if D[idx]!=t:
        print("NO")
        exit()
    idx+=1
print("YES")