from fractions import gcd

N,M = list(map(int, input().split()))
s = input()
t = input()

if s[0] != t[0]:
    print(-1)
    exit()
if s == t:
    print(N)
    exit()

saisho_kobaisu = (N * M) // gcd(N, M)
# print(saisho_kobaisu)

s_d = saisho_kobaisu // N
t_d = saisho_kobaisu // M

s_set = set([i * s_d + 1 for i in range(N)])
t_set = set([i * t_d + 1 for i in range(M)])

# print(s_set)
# print(t_set)
# print(s_set.intersection(t_set))
for idx in s_set.intersection(t_set):
    if (idx-1)//s_d > N or (idx-1)//t_d > M:
        break
    if s[(idx-1)//s_d] != t[(idx-1)//t_d]:
        print(-1)
        exit()

print(saisho_kobaisu)