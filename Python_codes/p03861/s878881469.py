s = input().split()

a = int(s[0])
b = int(s[1])
x = int(s[2])

def bet_ween(p, q):
    if p < 0:
        return 0
    else:
        return (p // q) + 1


fa = bet_ween(a-1, x)
fb = bet_ween(b, x)
answer = fb - fa
print(int(answer))