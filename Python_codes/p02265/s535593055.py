from collections import deque


n = int(input())
L = deque()

for i in range(n):
    com = input()
    if com[0] == 'i':
        C = com.split()
        L.appendleft(int(C[1]))
    else:
        if com[6] == 'F':
            L.popleft()
        elif com[6] == 'L':
            L.pop()
        else:
            C = com.split()
            x = int(C[1])
            try:
                L.remove(x)
            except:
                pass

print(*L)
