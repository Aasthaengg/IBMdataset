a,b,k = map(int,input().split())
if a >= k:
    ans1 = a-k
    ans2 = b 
if a < k:
    if (a+b) <= k:
        ans1 = 0
        ans2 = 0
    else:
        ans1 = 0
        ans2 = b-(k-a)
print(ans1,ans2)