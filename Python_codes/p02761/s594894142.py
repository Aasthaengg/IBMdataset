N, M = map(int, input().split())
if N > 1:
    number = [1] + [0] * (N-1)
else:
    number = [0]
SC = {}
for _ in range(M):
    s, c = map(int, input().split())
    if SC.get(s, c) != c:
        print(-1)
        exit()
    if N >= 2 and (s == 1 and c == 0):
        print(-1)
        exit()
    number[s-1] = c
    SC[s] = c
print("".join(map(str, number)))