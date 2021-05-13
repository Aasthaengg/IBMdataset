N = int(input())

ct = 0
for ct in range(1,11):
    pay = 1000 * ct
    if  pay >= N:
        tsuri = pay - N
        break

print(tsuri)
