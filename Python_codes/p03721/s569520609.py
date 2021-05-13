N, K = map(int, input().split())
Ans = [0] * (10**5 + 10)

for _ in range(N):
    a, b = map(int, input().split())
    Ans[a] += b

for i, ans in enumerate(Ans):
    K -= ans
    if K <= 0:
        print(i)
        exit()

