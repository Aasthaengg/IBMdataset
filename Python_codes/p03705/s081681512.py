# map(int, input().split())
N, A, B = map(int, input().split())
mn = A * (N - 1) + B
mx = B * (N - 1) + A
ans = mx - mn + 1
if ans < 0:
    print(0)
else:
    print(ans)