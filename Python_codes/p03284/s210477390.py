N, K = [int(i) for i in input().split()]

if N % K == 0:
    ans = 0
else:
    ans = 1
    
print(ans)