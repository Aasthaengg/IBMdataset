n = int(input())
A = list(map(int, input().split()))

#左から丹頂非増加、単調非減少を試して行って長い方を採用すれば良いO(N)
#値の増減の反転するポイントを探索する

ans = 1
tmp = 0
for i in range(1, n):
    if (A[i] - A[i-1]) * tmp < 0:
        ans += 1
        tmp = 0
    elif A[i] - A[i-1] != 0:
        tmp = A[i] - A[i-1]

print(ans)
