n = int(input())
S = input()
WE = [[] for _ in range(n)]
w = 0
e = 0

for i in range(n):
    if S[i] == "W":
        w += 1
    else:
        e += 1
    
    WE[i].append(w)
    WE[i].append(e)
    
ans = WE[n-1][1] - WE[0][1]

for i in range(1,n):
    res = WE[i-1][0] + (WE[n-1][1] - WE[i][1])
    ans = min(ans,res)
    
print(ans)