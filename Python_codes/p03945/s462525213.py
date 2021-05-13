S = input()
b = S[0]
x = [b]
for s in S[1:]:
    if b == s: continue
    x.append(s)
    b = s
print(len(x)-1)