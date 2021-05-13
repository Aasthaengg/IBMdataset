
N = int(input())
K = list(map(int,input().split()))
K = sorted(K,reverse=True)
"""
#print(K)
before_data = 0
before_data_before = 0
ans = 0 
for i in K :
    ans += before_data
    before_data_before = before_data
    before_data = i
"""
ans = 0 
for i,l in enumerate(K) :
    if (i == 0 ):
        ans += 0
    else :
        ans += K[i // 2]
print(ans)