N,A,B,C = map(int,input().split())
L = [int(input()) for i in range(N)]

def cost(group,target):
    res = 10*(len(group)-1)
    return res + abs(sum(group)-target)

ans = []
for i in range(1<<(2*N)):
    groupA = []
    groupB = []
    groupC = []
    for j in range(N):
        s = i>>(2*j)
        if (s & 3) == 3:
            groupA.append(L[j])
        elif (s & 2) == 2:
            groupB.append(L[j])
        elif (s & 1) == 1:
            groupC.append(L[j])
    
    if len(groupA)==0 or len(groupB)==0 or len(groupC)==0:
        pass
    else:
        ans.append(cost(groupA,A)+cost(groupB,B)+cost(groupC,C))
print(min(ans))