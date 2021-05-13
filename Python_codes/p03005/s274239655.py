#A
N, K= map(int, input().split())
a = N - K
if K > 1:
    ans = a
else:
    ans = 0
print(ans)
