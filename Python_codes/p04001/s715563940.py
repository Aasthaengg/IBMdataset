from itertools import product
s = input()
op = list(product(["", "+"], repeat=len(s)))
op = [a for a in op if not a[-1] == "+"]
ans = 0
for q in op:
    e = ""
    for w in range(len(q)):
        e += s[w] + q[w]
    ans += eval(e)
print(ans)