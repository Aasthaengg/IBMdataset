N = int(input())
Blue = {}
for _ in range(N):
    s = input()
    if s in Blue:
        Blue[s] += 1
    else:
        Blue[s] = 1

M = int(input())
Red = {}
for _ in range(M):
    t = input()
    if t in Red:
        Red[t] += 1
    else:
        Red[t] = 1

Max = 0
for item in Blue.items():
    s = item[0]
    v = item[1]
    if s in Red:
        v -= Red[s]
    Max = max(Max, v)
print(Max)