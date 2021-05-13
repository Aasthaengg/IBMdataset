def dfs(now1, now2, now3, d):
    if d==N:
        if min(now1, now2, now3)==0:
            return 10**18
            
        return abs(A-now1)+abs(B-now2)+abs(C-now3)
        
    res = 10**18
    res = min(res, dfs(now1+l[d], now2, now3, d+1)+10)
    res = min(res, dfs(now1, now2+l[d], now3, d+1)+10)
    res = min(res, dfs(now1, now2, now3+l[d], d+1)+10)
    res = min(res, dfs(now1, now2, now3, d+1))
    
    return res

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0)-30)