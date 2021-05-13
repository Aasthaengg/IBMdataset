S = input()
cnt = 0
for s in S[::2]:
    if s in {"R", "U", "D"}:
        cnt += 1
for s in S[1::2]:
    if s in {"L", "U", "D"}:
        cnt += 1
if cnt == len(S):
    print("Yes")
    exit()
print("No")

