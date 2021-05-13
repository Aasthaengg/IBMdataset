from collections import deque
s = [deque(input()) for _ in range(3)]
d = {"a":0, "b":1, "c":2}
D = {0:"A", 1:"B", 2:"C"}
player = 0
for _ in range(301):
    x = s[player].popleft()
    player = d[x]
    if not s[player]:
        print(D[player])
        exit()