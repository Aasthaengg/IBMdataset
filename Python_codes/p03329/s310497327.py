n = int(input())
dp = [None] * (n+1)
dp[1] = 1
dp[0] = 0
sixs = [6]
nines = [9]
i = 1
while sixs[i-1] * 6 <= n:
    sixs.append(sixs[i-1]*6)
    i += 1

i = 1
while nines[i-1] * 6 <= n:
    nines.append(nines[i-1]*9)
    i += 1
for current in range(2, n+1):
    smin = n
    for six in sixs:
        if current - six >= 0 and dp[current-six] != None:
            smin = min(smin, dp[current-six] + 1)
    nmin = n
    #print (smin, nmin)
    for nine in nines:
        if current - nine >= 0 and dp[current-nine] != None:
            nmin = min(nmin, dp[current-nine] + 1)
    #print (dp)
    dp[current] = min(dp[current-1] + 1, nmin, smin)
print (dp[n])
#print (dp)