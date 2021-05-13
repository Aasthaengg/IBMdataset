S = input()
loseCount = 0

for n in range(len(S)):
    if S[n] == "x":
        loseCount = loseCount + 1

if loseCount >= 8:
    print("NO")
else:
    print("YES")