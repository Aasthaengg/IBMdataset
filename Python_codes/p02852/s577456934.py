N, M = map(int, input().split())
S = input()

pos = N
step = []
isGoal = 1
while pos > 0:
    for i in range(M, 0, -1):
        if pos - i <= 0:
            step.append(pos)
            pos = 0
        elif S[pos - i] == '0':
            step.append(i)
            pos -= i
        else:
            continue
        break
    else:
        isGoal = 0
        break

if isGoal:
    print(*[x for x in reversed(step)])
else:
    print(-1)
