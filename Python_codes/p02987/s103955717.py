S = input()
s1 = 0

for s in S:
    if s == S[0]:
        s1 += 1

print("Yes" if len(set(S)) == 2 and s1 == 2 else "No")