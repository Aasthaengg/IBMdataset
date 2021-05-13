N = int(input())

ppl = list(input())

buff = []
w = 0
e = ppl[1:].count('E')
for i in range(N):
    if i > 0:
        w += (ppl[i-1] == 'W' and 1 or 0)
    if i > 0:
        e -= (ppl[i] == 'E' and 1 or 0)
    n = w+e
    buff.append(n)

print(min(buff))