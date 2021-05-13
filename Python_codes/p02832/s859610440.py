n  = int(input())
ai = list(map(int, input().split()))

step = 1

for i in range(len(ai)):
    if ai[i] != step:
        ai[i] = 0
    else:
        step += 1

if sum(ai) == 0:
    print(-1)
else:
    print(ai.count(0))