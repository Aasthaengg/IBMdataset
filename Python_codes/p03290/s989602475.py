D, G = list(map(int,input().split()))
p = []
c = []

for i in range(D):
    in1, in2 = list(map(int,input().split()))
    p.append(in1)
    c.append(in2)
    
ans = 10 ** 9 + 7
for x in range(2 ** D):
    b = str(format(x, '010b'))
    score = 0
    res = 0
    not_perfect = 0
    for i in range(D):
        if b[-(i + 1)] == "1": 
            score += (p[i] * 100 * (i + 1) + c[i])
            res += p[i]
        else:
            not_perfect = i
    rest = G - score
    if rest > 0:
        s = 100 * (not_perfect + 1)
        for i in range(p[not_perfect]):
            res += 1
            rest -= s
            if rest <= 0:
                break
        if rest > 0:
            res = 10 ** 9 + 7
    ans = min(ans, res)
    
print(ans)