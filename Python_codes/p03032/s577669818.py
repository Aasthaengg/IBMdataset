def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    V *= 2
    ans = 0
    for i in range(N+1):
        for j in range(N-1,2*N):
            num = j-i+1
            if num>K or num>N or num == 0:
                continue
            lis = V[i:j+1]
            lis.sort()
            margin = K-num
            m = sum(lis)
            k = 0
            while k < margin and k < num and lis[k]<0 :
                m -= lis[k]
                k += 1
            ans = max(ans,m)
    return ans
print(solve())