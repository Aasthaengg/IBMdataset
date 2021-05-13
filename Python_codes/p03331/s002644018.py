N = int(input())
ans = float('inf')
for i in range(1,N):
    A = i
    B = N - i
    Sum = 0
    for power in range(4,-1,-1):
        q_a,r_a = divmod(A,10**power)
        A = r_a
        q_b,r_b = divmod(B,10**power)
        B = r_b
        Sum += q_a + q_b
    ans = min(Sum, ans)
print(ans)
