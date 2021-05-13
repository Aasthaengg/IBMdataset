#<B>
import bisect
n, k = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
ans = n
for i in h:
    if i < k:
        ans -= 1

print(ans)
        
