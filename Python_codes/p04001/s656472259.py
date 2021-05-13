from itertools import product

S = input()

s = 0
for bits in product((False, True), repeat=len(S) - 1):
    buf = S
    for i in range(len(bits)):
        if bits[i]:
            sep = len(S) - (i + 1)
            buf = buf[:sep] + ' ' + buf[sep:]
    s += sum(map(int, buf.split()))

print(s)
