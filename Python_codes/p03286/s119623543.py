# input
N = int(input())

# check
if N == 0:
    print(0)
    exit(0)

r_bits = ""
p = 0
d = 0
while N + p:
    if (N & 1) ^ p:
        r_bits += '1'
        if d ^ p:
            p ^= 1
    else:
        r_bits += '0'
    N >>= 1
    d ^= 1

print(r_bits[::-1])