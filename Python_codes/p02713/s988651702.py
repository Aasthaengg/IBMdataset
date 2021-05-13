def euclid(a, b):
    global l
    if b == 0:
        return a
    else:
        ch = l[a][b]
        if ch == 0:
            return euclid(b, a%b)
        else:
            return ch

def gcd(a, b, c):
    global l
    d = l[c][b]
    if d == 0:
        d = euclid(c, b)
        l[c][b] = d

    e = l[max(d, a)][min(d, a)]
    if e == 0:
        e = euclid(max(d, a), min(d, a))
        l[max(d, a)][min(d, a)] = e

    return e

K = int(input())
ans = 0
l = []
for i in range(K+1):
    l.append([0]*(K+1))

for i in range(1, K+1):
    for j in range(i, K+1):
        for k in range(j, K+1):
            num = gcd(i, j, k)
            if i == j:
                if j == k:
                    ans += num
                else:
                    ans += 3*num
            else:
                if j == k:
                    ans += 3*num
                else:
                    ans += 6*num

print(ans)