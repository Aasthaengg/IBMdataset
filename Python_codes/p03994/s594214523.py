S = list(input())
N = len(S)
K = int(input())

for i in range(N - 1):
    d = (ord("a") - ord(S[i])) % 26
    if d <= K:
        S[i] = "a"
        K -= d

S[-1] = chr((ord(S[-1]) - ord("a") + K) % 26 + ord("a"))
print("".join(S))