N, T = map(int, input().split())
A = [int(x) for x in input().split()]
buy = A[0]
max_profit = 0
ans = 1
for i in range(1,N):
    if A[i] > buy:
        if A[i] - buy > max_profit:
            max_profit = A[i] - buy
            ans = 1
        elif A[i] - buy == max_profit:
            ans += 1
    else:
        buy = A[i]
print(ans)
