D, G = map(int, input().split())
G //= 100
P = [] 
C = []
for i in range(1, D+1):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c//100)

scores = []
nums = []
for i in range(0, 2**D):
    score = 0
    num = 0
    remain = []
    for j in range(D):
        if (i>>j)&1:
            score += P[j]*(j+1) + C[j]
            num += P[j]
        else:
            remain.append(j)
    if score >= G:
        scores.append(score)
        nums.append(num)
    else:
        remain = sorted(remain, reverse=True)
        nokori = G - score
        for r in remain:
            if P[r] > -(-nokori // (r+1)):
                num += -(-nokori // (r+1))
                nums.append(num)
                break
print(min(nums))