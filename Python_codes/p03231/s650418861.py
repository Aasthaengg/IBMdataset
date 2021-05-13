N, M = map(int, input().split())
S = list(input())
T = list(input())

if S[0] != T[0]:
    print(-1)
    exit()

# lcmで異なる文字が重なるようならダメ。そうでなければOK


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


l = lcm(N, M)

s = l // N
t = l // M
# print(f'{s=}, {t=}')
S_set = set([s * i for i in range(N)])
T_set = set([t * i for i in range(M)])

_set = S_set & T_set
# print(f'{S_set=}, {T_set=}, {_set=}')

for i in _set:
    if S[i // s] != T[i // t]:
        print(-1)
        exit()
print(l)
# a c p |
# a  e  |
