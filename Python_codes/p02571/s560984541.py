S = list(input())
T = list(input())
ls = len(S)
lt = len(T)
ans = lt
for i in range(ls):
    temp = 0
    if i+lt > ls:
        break
    subS = S[i:i+lt]
    for ss, st in zip(subS, T):
        if ss != st:
            temp += 1
    ans = min(ans, temp)
print(ans)