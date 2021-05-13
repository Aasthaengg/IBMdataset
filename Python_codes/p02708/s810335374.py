N,K = list(map(int,input().split()))

def get_ans(i):
    ans = i*(N+1) - i**2 +1
    ans = max(0,ans)
    return ans

ans=0
for i in range(K,N+2):
    ans_= get_ans(i)
    ans+=ans_
#     print(ans_,ans)
    
print(ans%(10**9+7))