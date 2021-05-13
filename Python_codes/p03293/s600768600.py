S, T = input(), input()

L = len(S)

ok = False

for i in range(L):
    if T == S[i:L] + S[0:i]:
        ok = True

print("Yes" if ok else "No")
