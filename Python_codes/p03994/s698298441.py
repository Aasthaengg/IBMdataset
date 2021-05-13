S = list(input())
K = int(input())

for i, s in enumerate(S):
    if s == "a":
        pass
    elif ord('z') - ord(s) + 1 <= K:
        S[i] = 'a'
        K -= ord('z') - ord(s) + 1

K %= 26
S[-1] = chr((ord(S[-1]) - ord('a') + K) % 26 + ord('a'))

print("".join(S))
