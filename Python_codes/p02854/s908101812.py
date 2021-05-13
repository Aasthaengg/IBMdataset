n = int(input())
L = list(map(int,input().split()))

diff = 10**10
sum1 = sum(L)
l_sum = 0
ans = 10**10

for i in range(n-1):
    l_sum+=L[i]
    diff = abs(l_sum- sum1 + l_sum)
    ans = min(ans,diff)
    
print(ans)