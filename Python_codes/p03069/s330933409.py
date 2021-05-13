N = int(input())
S = input()
t_min = min(S.count("#"), S.count("."))
S_first = 0
S_second = S.count(".")
for i in range(0,N):
    if S[i] == "#":
        S_first += 1
    else:
        S_second -= 1
    t = S_first + S_second
    t_min = min(t_min, t)
print(t_min)