N=int(input())
P=list(map(int,input().split()))
ans = 0
for i in range(N):
    if i == 0:
        ans += 1
        mini = P[0]
    else:
        if mini >= P[i]:
            mini = P[i]
            ans += 1
        #print(P[0:i+1],P[i],min(P[0:i+1]),i)
        #if min(P[0:i+1]) == P[i]:
            #ans += 1
print(ans)
