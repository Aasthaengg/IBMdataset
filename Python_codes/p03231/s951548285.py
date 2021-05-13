N, M = map(int, input().split(' '))
S = input()
T = input()

def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    else:
        return gcd(b, a - b)

lcm = N * M // gcd(N, M)
s_c_dict = dict([[j, S[i]] for i, j in enumerate(range(0, lcm, lcm//N))])
for i, j in enumerate(range(0, lcm, lcm//M)):
    if j in s_c_dict:
        if s_c_dict[j] != T[i]:
            print(-1)
            exit()
print(lcm)
