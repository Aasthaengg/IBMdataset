O = input()
E = input() + ' '

P = ''

for i in range(len(O)):
    P += O[i] + E[i]

print(P.rstrip())