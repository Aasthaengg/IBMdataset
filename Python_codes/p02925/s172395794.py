import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque

N = int(readline())
m = map(int,read().split())
A = [None] + list(map(deque,zip(*[m]*(N-1))))

day = 0
rest = N*(N-1)
cand = set(range(1,N+1))
while rest:
    day += 1
    match_player = set()
    for i in cand:
        if not A[i]:
            continue
        if A[A[i][0]][0] == i:
            match_player.add(i)
            match_player.add(A[i][0])
    if not match_player:
        break
    rest -= len(match_player)
    cand.clear()
    for i in match_player:
        cand.add(i)
        A[i].popleft()
        if A[i]:
            cand.add(A[i][0])

answer = day if rest == 0 else -1
print(answer)