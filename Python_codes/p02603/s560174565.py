N = int(input())
A = list(map(int, input().split()))
A = [1000] + A + [0]

ans = 1000
stock = 0

for i, a in enumerate(A):
    if i > 0 and i < N + 1:
        if A[i-1] >= a and A[i+1] >= a:
            stock += ans // a
            ans -= a * (ans // a)

        if A[i-1] <= a and A[i+1] <= a:
            ans += stock * a
            stock = 0
        
print(ans)

