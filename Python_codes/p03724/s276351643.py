
n,m = list(map(int, input().split()))
times = [0 for i in range(n)]
for i in range(m):
    t = list(map(int, input().split()))
    times[t[0]-1]+=1
    times[t[1]-1]+=1

ans = 1
for i in range(n):
    ans *= (times[i]+1)%2
    
if(ans==1):
    print("YES")
else:
    print("NO")



