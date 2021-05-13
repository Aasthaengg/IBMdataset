n, m = map(int, input().split())

smi = [ None ] * m

for i in range(m):
    k, *si = map(lambda x: int(x) - 1, input().split())

    smi[i] = si

pi = list(map(int, input().split()))

def emitable(bit_pattern, i):
    si = smi[i]
    px = pi[i]
    py = 0

    for s in si:
        py += (bit_pattern & (2 ** s)) >> s

    return px == (py % 2)

count = 0

for bi in range(2 ** n):
    if all(emitable(bi, i) for i in range(m)):
        count += 1

print(count)