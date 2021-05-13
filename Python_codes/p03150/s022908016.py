S = input()
N = len(S)

target = "keyence"
T = len(target)

for i in range(8):
    cand = S[:i] + S[N - T + i :]
    if cand == target:
        print("YES")
        break
else:
    print("NO")