S = input()
N = len(S) - 1

sum = 0
for bit in range(2 ** N):
    E = S[0]
    for i in range(N):
        if (bit & (1 << i)):
            E += ' + '
        E += S[i + 1]
    sum += eval(E)

print(sum)