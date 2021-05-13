from collections import deque

N = int(input().strip("\n"))
ALL = N*(N-1)//2
A = [deque(list(map(lambda x :int(x)-1, input().split()))) for _ in range(N)]

day = 0
candidates = set(range(N))
while len(candidates)>0:
    day += 1
    nextday = set()
    checked = set()
    #print(candidates)
    for candidate in candidates:
        if len(A[candidate]) == 0:
            continue
        if candidate in checked:
            continue
        opponent = A[candidate][0]
        if opponent in checked:
            continue
        if A[opponent][0] == candidate:
            A[opponent].popleft()
            A[candidate].popleft()
            nextday.add(candidate)
            nextday.add(opponent)
            checked.add(candidate)
            checked.add(opponent)
    candidates = nextday

for p in A:
    if len(p) > 0:
        print(-1)
        break
else:
    print(day-1)