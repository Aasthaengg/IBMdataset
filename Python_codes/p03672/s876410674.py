def is_even_str(s):
    l = len(s)
    if l % 2 != 0:
        return False
    return s[:l // 2] == s[l // 2:]


S = input()[:-2]
while not is_even_str(S):
    S = S[:-2]
print(len(S))
