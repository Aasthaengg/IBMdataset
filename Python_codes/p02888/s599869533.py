import bisect
#二分探索をするライブラリ

n = int(input())
L = sorted(map(int,input().split()))
ans = 0

# c <= b <= a とする

for i in range(n-2):
    for j in range(i+1,n-1):
        a = L[n-1-i]
        b = L[n-1-j]
        
        if a-b < b:
            ans += (n-1-j) - bisect.bisect_left(L,a-b+1)
        
print(ans)