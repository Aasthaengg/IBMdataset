def next_koch(n):
    turn60 = 0.5 + 3 ** 0.5 * 0.5j
    n_next = [n[0]]
    for i in range(1, len(n)):
        s = (n[i - 1] * 2 + n[i]) / 3
        t = (n[i - 1] + n[i] * 2) / 3
        u = (t - s) * turn60 + s
        n_next +=[s, u, t, n[i]]
    return n_next

p1 = 0 + 0j
p2 = 100 + 0j
koch = [p1, p2]

n = int(input())
for i in range(n):
    koch = next_koch(koch)

for z in koch:
    print("{:.8f} {:.8f}".format(z.real, z.imag))