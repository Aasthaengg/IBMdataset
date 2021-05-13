N = int(input()) - 1
s = ''

M = 0
for i in range(1, 1000000):
    M += 26 ** i
    if M > N:
        break

N -= (M - 26**i)

for j in reversed(range(i)):
    K = N // (26 ** j)
    s += chr(K + 97)
    N -= K * (26 ** j)

print(s)