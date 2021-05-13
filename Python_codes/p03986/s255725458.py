import sys
X = sys.stdin.readline().rstrip()
S = 0
T = 0
ans = 0
for x in X:
    if x == "S":
        S += 1
    else:
        if not S:
            ans += 1
        else:
            S -= 1
ans += S
print(ans)