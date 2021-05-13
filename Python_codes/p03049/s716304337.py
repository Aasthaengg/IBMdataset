N = int(input())
S = [input() for _ in range(N)]
 
# 文字列にABが入ってる数 + 組み合わせて入る数
# 文字列にABが入ってる数 + f(Aで終わる数, Bで始まる数, Bで始まりAで終わる数)
include = 0
sb = 0
fa = 0
sbfa = 0
for s in S:
    include += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        sbfa += 1
    elif s[0] == 'B':
        sb += 1
    elif s[-1] == 'A':
        fa += 1

def calc_comb(sb, fa, sbfa):
    if sbfa == 0:
        return min(sb, fa)
    elif max(sb, fa)==0:
        return sbfa -1
    else:
        return sbfa + min(sb, fa)

print(include + calc_comb(sb, fa, sbfa))
