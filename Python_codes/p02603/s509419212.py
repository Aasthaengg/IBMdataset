N = int(input())
A = list(map(int, input().split()))
money = 1000
cnt = 0
if A[0] < A[1]:
    cnt += 1000 // A[0]
    money = money % A[0]
for i in range(1, N-1):
    if A[i] <= A[i - 1] and A[i] < A[i + 1]:
        cnt += money // A[i]
        money = money % A[i]
    elif A[i] >= A[i-1] and A[i] > A[i + 1]:
        money += cnt * A[i]
        cnt = 0
if cnt != 0:
    money += cnt * A[N - 1]
    cnt = 0
print(money)