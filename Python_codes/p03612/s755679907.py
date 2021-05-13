N = int(input())
*P, = map(int, input().split())

ans = 0
for i in range(N-1):
    if P[i]==(i+1):
        temp = P[i]
        P[i] = P[i+1]
        P[i+1] = temp
        ans = ans + 1
if P[N-1]==(N):
    ans = ans + 1
print(ans)