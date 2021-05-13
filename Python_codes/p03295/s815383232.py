N, M = map(int, input().split())
bridge = [list(map(int, input().split())) for i in range(M)]
bridge = sorted(bridge, key = lambda x:x[1])
ans = 1
edge = bridge[0][1]
for i in range(1,M):
    if bridge[i][0] < edge:
        continue
    else:
        edge =bridge[i][1]
        ans += 1
print(ans)
    
    
    
