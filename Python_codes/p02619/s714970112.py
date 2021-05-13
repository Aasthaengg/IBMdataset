D = int(input())
C = list(map(int, input().split()))

S = [list(map(int, input().split())) for _ in range(D)]

contest = [0 for _ in range(26)]
ans = 0

for i in range(D):
    t = int(input())
    contest[t-1] = i+1
    ans += S[i][t-1]
    for j, con in enumerate(contest):
        if con:
            ans -= C[j]*(i+1-con)
        else:
            ans -= C[j]*(i+1)
    print(ans)