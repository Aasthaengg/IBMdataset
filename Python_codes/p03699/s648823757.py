N = int(input())
S = [int(input()) for _ in range(N)]
sumS = sum(S)
if all(s % 10 == 0 for s in S):
    print(0)
elif sumS % 10 != 0:
    print(sumS)
else:
    S = sorted(S)
    for s in S:
        if s % 10 != 0:
            t = s
            break
    print(sumS - t)