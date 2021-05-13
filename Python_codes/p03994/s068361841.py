s = list(input())
K = int(input())

for i in range(len(s)):
    need = (123-ord(s[i]))%26
    if need <= K:
        s[i] = "a"
        K -= need
if 0 < K:
    tmp = ord(s[-1]) + K%26
    tmp -= 26 if 123 <= tmp else 0
    s[-1] = chr(tmp)
print("".join(s))