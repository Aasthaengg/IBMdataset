N,C = map(int, input().split())
L = [[int(a) for a in input().split()] for _ in range(N)]

ans = [0]*C
chan = [0]*C
L.sort()
for i in range(N):
    for j in range(C):
        if ans[j] == L[i][0] and chan[j] == L[i][2]:
            ans[j] = L[i][1]
            break
        elif ans[j] < L[i][0]:
            ans[j] = L[i][1]
            chan[j] = L[i][2]
            break
    ans.sort(reverse=True)
    
num = 0
for i in range(C):
    if ans[i] > 0:
        num += 1
        
print(num)