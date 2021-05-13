S = input()
K = int(input())
V = []
for e in S:
    V.append(ord(e)-97)
for i in range(len(S)):
    if S[i] == 'a':
        continue
    if K < 26-V[i]:
        pass
    else:
        K -= 26-V[i]
        V[i] = 0
V[-1] += K
V[-1] %= 26
V = [chr(e+97) for e in V]
print("".join(V))
