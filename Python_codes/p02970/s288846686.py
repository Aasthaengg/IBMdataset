N, D = list(map(int, input().split()))

s = D * 2 + 1
ans = N // s
if N % s != 0:
    ans = N // s + 1

print(ans)