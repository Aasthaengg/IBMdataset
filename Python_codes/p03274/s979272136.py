n, k = map(int, input().split())
x = list(map(int, input().split()))
start = 0 # i-1本目とi本目の間に0がある

ans = 10**9
for i in range(n-k+1):
    tmp_ans = min(
        abs(x[i]) + abs(x[i+k-1]-x[i]),
        abs(x[i+k-1]) + abs(x[i+k-1]-x[i])
    )
    if tmp_ans < ans:
        ans = tmp_ans

print(ans)
