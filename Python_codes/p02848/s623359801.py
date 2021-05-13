import string

n = int(input())
s = input()
ALPHABET = string.ascii_uppercase

ans = ''
for s_ in s:
    idx = ALPHABET.index(s_)
    idx_ = idx + n if idx + n < 26 else idx + n - 26
    ans += ALPHABET[idx_]
print(ans)