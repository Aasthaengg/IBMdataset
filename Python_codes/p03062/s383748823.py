N = int(input())
cnt = 0
m = float("inf")
S = 0
for a in map(int, input().split()):
    m = min(m, abs(a))
    if a < 0:
        cnt += 1
        S -= a
    else:
        S += a
if cnt%2:
    print(S-2*m)
else:
    print(S)