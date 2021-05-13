def popcount(n):
    return bin(n).count("1")

def f(n):
    cnt = 0
    while n != 0:
        n %= popcount(n)
        cnt += 1
    return cnt

N = int(input())
S = input()

pcnt_X = S.count("1")
X = int(S, 2)

Xm = X % (pcnt_X - 1) if pcnt_X - 1 > 0 else float("inf")
Xp = X % (pcnt_X + 1)

for i, s in enumerate(S):
    if s == "0":
        x = (Xp + pow(2, N - 1 - i, pcnt_X + 1)) % (pcnt_X + 1)
        print(1 + f(x))
    elif pcnt_X - 1 > 0:
        x = (Xm - pow(2, N - 1 - i, pcnt_X - 1)) % (pcnt_X - 1)
        print(1 + f(x))
    else:
        print(0)