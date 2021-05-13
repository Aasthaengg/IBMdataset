N,K = map(int,input().split())
lst = list(map(int,input().split()))

ans = 0
for i in range(K):
    ans += min(lst)
    lst.remove(min(lst))
    
print(ans)