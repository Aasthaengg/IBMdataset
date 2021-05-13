import fractions

n, m = map(int, input().split())
s = input()
t = input()

l = n*m//fractions.gcd(n, m)

s_dic = {i * l//n + 1: s[i] for i in range(n)}
t_dic = {i * l//m + 1: t[i] for i in range(m)}

dup_idx = set(s_dic.keys()) & set(t_dic.keys())

for d in dup_idx:
    if s_dic[d] != t_dic[d]:
        print(-1)
        break
else:
    print(l)
