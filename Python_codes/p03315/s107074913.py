S = input()

n = 0

i = 0

while i < 4:
    if S[i] == '+':
        n += 1
    else:
        n -= 1
    i += 1

print(n)