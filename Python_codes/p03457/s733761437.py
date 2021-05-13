N = int(input())
txy = [[0,0,0] for i in range(N+1)]
for i in range(1,N+1):
    txy[i] = list(map(int,input().split()))

ans = 'Yes'
for i in range(1,N+1):
    dist = abs(txy[i][1]-txy[i-1][1])+abs(txy[i][2]-txy[i-1][2])
    dt   = txy[i][0]-txy[i-1][0]
    
    if dist%2 != dt%2 or dist>dt:
        ans = 'No'
        
print(ans)