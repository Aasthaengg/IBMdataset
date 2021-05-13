def tetra(x):
    ret = ""
    for _ in range(3):
        ret = str(x%4) + ret
        x = (x-x%4)//4
    return ret
n = int(input())
mod = 10**9+7
if n<=2:
    print(4**n)
    exit()
DP = [[0]*64 for i in range(n+1)]
for i in range(64):
    if tetra(i) not in ["023","032","203"]:
        DP[0][i] = 1
for i in range(1,n+1):
    for j in range(64):
        tj = tetra(j)
        jprelist = [j//4+l*16 for l in range(4)]
        for jprev in jprelist:
            tjp = tetra(jprev)
            if ((tjp[1:]  in ["02","20"] or tjp[:2] == "02" or tjp == "012")
                and (tj[2] == "3")) or (tjp[1:]  == "03" and tj[2] == "2"):
                continue
            else:            
                DP[i][j] = (DP[i][j]+DP[i-1][jprev])%mod
print(sum(DP[n-3])%mod)