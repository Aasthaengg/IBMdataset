n = int(input())
S = [int(input()) for _ in range(n)]
S.sort()

score = sum(S)
if score % 10 == 0:
    for s in S:
        if s % 10 != 0:
            score -= s
            break

print(0 if score % 10 == 0 else score)