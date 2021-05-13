N = int(input())
Ss, Ts = input().split()

anss = ''
for S, T in zip(Ss, Ts):
    anss += S + T

print(anss)
