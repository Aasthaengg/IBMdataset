def judge_kaibun(p):
    p = str(p)
    return p==p[::-1]

A, B = map(int, input().split())

ans = 0

for i in range(A, B+1):
    ans += judge_kaibun(i)

print(ans)