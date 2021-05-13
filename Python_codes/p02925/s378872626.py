from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
game = {}

for i in range(1, n+1):
    game[i] = deque((map(int, input().split())))

count = 0
final = n*(n-1)//2
done = []

finish = [0] * (n + 1)
for me in range(1, n + 1):
    if finish[me] == 1 or game[me] == deque([]):
        continue

    you = game[me][0]
    if finish[you] == 1:
        continue
    else:
        if game[you][0] == me:
            done.append(you)
            done.append(me)
            finish[game[you].popleft()] = 1
            finish[game[me].popleft()] = 1
            possible = True
            count += 1
        else:
            continue

for day in range(2, 1000000):
    finish = [0]*(n+1)
    possible = False
    new_done = []
    for me in done:
        if finish[me] == 1 or game[me] == deque([]):
            continue

        you = game[me][0]
        if finish[you] == 1:
            continue
        else:
            if game[you][0] == me:
                finish[game[you].popleft()] = 1
                finish[game[me].popleft()] = 1
                new_done.append(me)
                new_done.append(you)
                possible = True
                count += 1
            else:
                continue
    done = new_done
    if not possible:
        print(-1)
        exit()

    if count == final:
        print(day)
        exit()