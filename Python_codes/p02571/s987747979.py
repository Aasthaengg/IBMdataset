S = list(input())
T = list(input())

res = len(T)

for i in range(len(S) - len(T) + 1):
    cnt = 0
    smallS = S[i:i+len(T)]
    for s, t in zip(smallS, T):
        if s == t:
            cnt += 1
    if (len(T) - cnt) < res:
        res = len(T) - cnt

print(res)