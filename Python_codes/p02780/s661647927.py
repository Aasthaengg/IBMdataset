memo = [0] * 200001 
def kitaichi(kazu):
    global memo
    ans = 0
    if memo[kazu] == 0:
        for i in range(1,kazu+1):
            ans += i * (1 / kazu)
        memo[kazu] = ans
    return memo[kazu]

n,k = map(int,input().split())
p = list(map(int,input().split()))
ans = 0
max_p = 0
for j in range(k):
    ans += kitaichi(p[j])
#print(ans)
max_p = ans
for i in range(n-k):
    #print(ans,kitaichi(p[i+k]),kitaichi(p[i]))
    ans = ans + kitaichi(p[i+k]) - kitaichi(p[i])
    #print(ans)
    max_p = max(ans,max_p)
print(max_p)