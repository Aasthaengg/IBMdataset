n, m = map(int, input().split())
k = []
s = []
for _ in range(m):
    ks = list(map(int, input().split()))
    _k = ks[0]
    _s = [ks[i] for i in range(1, len(ks))]
    k.append(_k)
    s.append(_s)
p = list(map(int, input().split()))

def get_bits_pattern(n):
    bits_pattern = []
    for i in range(2**n):
        bits = [False]*n

        for j in range(n):
            if i >> j & 1:
                bits[j] = True
        bits_pattern.append(bits)
    return bits_pattern

bits_pattern = get_bits_pattern(n)

pattern_counter = 0
for bits in bits_pattern:
    is_on = True
    for _s, _p in zip(s, p):
        counter = 0
        for __s in _s:
            if bits[__s-1]:
                counter += 1
        if _p != counter % 2:
            is_on = False
    if is_on:
        pattern_counter += 1

print(pattern_counter)