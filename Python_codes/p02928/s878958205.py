N, K = map(int,input().split())
A = [int(i) for i in input().split()]
a = 0
b = 0
mod = 10**9+7
for i in range(N) :
    for j in range(N) :
        if A[i]>A[j] :
            if i < j :
                a += 1
            else :
                b += 1
ans = ( a * ((K+1)*K) // 2 + b * (K*(K-1)) // 2) %mod
print(ans)