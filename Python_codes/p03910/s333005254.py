N = int(input())

ans = []
sm = 0
for i in range(1, N+1):
    sm += i
    ans.append(i)
    if sm >= N:
        exclusion = -1
        if sm-N != 0:
            exclusion = sm-N

        for a in ans:
            if a != exclusion:
                print(a)
        break
