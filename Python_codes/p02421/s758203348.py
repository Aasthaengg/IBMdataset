# 9_C
n = int(input())
score_t, score_h = 0, 0
for i in range(n):
    t, h = input().split()
    if t > h:
        score_t += 3
    elif h > t:
        score_h += 3
    else:
        score_t += 1
        score_h += 1
print(f"{score_t} {score_h}")
