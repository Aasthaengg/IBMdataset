#B問題
N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

count = [0 for i in range(N)]
now = [-1 for i in range(N+1)]
for i in range(N):
    if P[i] == 1:
        now[P[i]-1] = P[i]
        count[P[i]-1]+=1
    elif now[P[i]-2] == -1:
        now[P[i]-1] = P[i]
        count[P[i]-1]+=1
    else:
        now[P[i]-1] = P[i]
        count[P[i]-1] = count[P[i]-2]+1
        
#print(count,now)
MAX = max(count)
ans = N-MAX
print(ans)