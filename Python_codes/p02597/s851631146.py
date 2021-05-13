N = int(input())
S = input()
redPref = [0 for i in range(0, N)]

if S[0] == 'R':
    redPref[0] += 1

for i in range(1, N):
    redPref[i] += redPref[i - 1]
    if S[i] == 'R':
        redPref[i] += 1

def query(l, r, pref):
    a, b = 0, pref[r]
    if l - 1 >= 0:
        a = pref[l - 1]
    return b - a


ans = min(N - redPref[-1], redPref[-1])

for i in range(0, N - 1):
    leftRed = query(0, i, redPref)
    leftWhite = i - leftRed + 1

    rightRed = query(i + 1, N - 1, redPref)
    rightWhite = ((N - 1) - (i + 1) + 1) - rightRed

    swaps = min(leftWhite, rightRed)
    leftWhite -= swaps
    rightRed -= swaps
    leftRed += swaps
    rightWhite += swaps

    ans = min(ans, leftWhite + rightRed + swaps)

print(ans)
