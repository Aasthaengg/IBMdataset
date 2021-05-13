N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    #i人目の勇者の戦闘
    rem = B[i] #残りの倒せるモンスター
    
    if A[i] >= rem:
        ans += rem
        continue
    else:
        rem -= A[i]
        ans += A[i]

    if A[i+1] >= rem:
        ans += rem
        A[i+1] -= rem
    else:
        ans += A[i+1]
        A[i+1] = 0
print(ans)