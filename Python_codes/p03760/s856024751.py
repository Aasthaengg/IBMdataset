O = input()
E = input()

res = ''
for i in range(len(O)):
    if i >= len(E):
        res += O[i]
    else:
        res += O[i] + E[i]

print(res)