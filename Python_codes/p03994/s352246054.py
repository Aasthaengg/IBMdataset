S = input()
N = len(S)
K = int(input())
T = []
for i in range(N):
    s = ord(S[i]) - 97
    a = (26-s) % 26
    if a <= K:
        K -= a
        T.append("a")
    else:
        T.append(S[i])
T[-1] = chr((ord(T[-1]) - 97 + K) % 26 + 97)
print("".join(T))