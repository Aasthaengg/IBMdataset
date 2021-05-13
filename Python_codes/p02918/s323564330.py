N, K = map(int, input().split())
S = input()
x, y = 0, 0
if S[0] == "L":
    y += 1
if S[-1] == "R":
    y += 1
x = S.count("RL")
if x:
    if x > K:
        x -= K
        K = 0
    else:
        K -= x
        x = 0
if K > 0:
    y = max(1, y - K)
print(N - 2 * x - y)