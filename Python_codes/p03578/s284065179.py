N = int(input())
D = list(map(int, input().split(" ")))
M = int(input())
T = list(map(int, input().split(" ")))
D.sort()
T.sort()

t = 0

for d in D:
    if t < len(T) and T[t] == d:
        t += 1
        d += 1

    if t == len(T):
        break

print('YES' if t == len(T) else 'NO')