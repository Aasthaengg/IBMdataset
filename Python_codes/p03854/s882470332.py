S = input()[::-1]

cand = {'maerd', 'remaerd', 'esare', 'resare'}

res = 'YES'

while len(S):
    orig = S
    for w in cand:
        if S.startswith(w):
            S = S[len(w):]
    if orig == S:
        res = 'NO'
        break

print(res)