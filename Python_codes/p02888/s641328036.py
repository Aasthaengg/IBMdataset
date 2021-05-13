import bisect

N = int(input())
L = list(map(int,input().split()))
L.sort()

# print(L)

ans=0
for a_idx in range(len(L)):
    a = L[a_idx]
    for b_idx in range(a_idx+1,len(L)):
        b = L[b_idx]
        c_low = b - a
        c_up = a + b - 1
        
        c_low_idx = bisect.bisect(L,c_low)
        c_up_idx = bisect.bisect(L,c_up)
        
#         print('=====')
#         print(a,b)
#         print(c_low_idx,c_up_idx)
        
        c_low_idx = max(b_idx,c_low_idx)
        
        ans += max(0,c_up_idx-c_low_idx-1)
#         print(ans,c_low_idx,c_up_idx)
print(ans)