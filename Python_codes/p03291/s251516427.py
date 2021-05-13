MOD = 10 ** 9 + 7
S = list(input())

n = 1
a = 0
ab = 0
abc = 0
for s in S:
    if s == 'A':
        a += n
    elif s == 'B':
        ab += a
    elif s == 'C':
        abc += ab
    else: #s == '?'
        abc = 3 * abc + ab
        ab = 3 * ab + a
        a = 3 * a + n
        n *= 3
    abc %= MOD
    ab %= MOD
    a %= MOD
    n %= MOD
    # print (a, ab, abc)
# print (a)
# print (ab)
print (abc)