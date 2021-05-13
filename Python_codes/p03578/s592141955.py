from collections import Counter
N = int(input())
D=list(map(int,input().split()))
M = int(input())
T=list(map(int,input().split()))

C=Counter(D)

for t in T:
    if C[t]<=0:
        print("NO")
        exit()
    else:
        C[t]-=1
print("YES")
