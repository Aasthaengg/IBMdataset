# compiled by pythran
"""
#pythran export main2()
import numpy as np
i8 = np.int64
MOD = 1000000007


def mod_inv(mod, a):
    old_t, t = 0, 1
    old_r, r = mod, a

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t

    return old_t % mod


def combine(n, k, mod):
    if k > n // 2:
        k = n - k
    u = 1
    for i in range(n - k + 1, n + 1):
        u = u * i % mod

    v = 1
    for i in range(1, k + 1):
        v = v * i % mod

    return u * mod_inv(mod, v) % MOD


def main(in_file):
    stdin = open(in_file)
    X, Y = [int(x) for x in stdin.readline().split()]
    m1 = X + Y
    if m1 % 3 == 0:
        m = m1 // 3
        if X < m or Y < m:
            print(0)
        else:
            print(combine(m, X - m, MOD))
    else:
        print(0)


def main2():
    main('/dev/stdin')
"""
import os, sys
p = os.path.dirname(__file__)
pymain = os.path.join(p, "a.out")
if len(sys.argv) == 1:
    import subprocess
    if p == "":
        pymain = "./" + pymain
    subprocess.call(pymain)
else:
    import gzip, base64, stat
    gz = b'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'
    bin = gzip.decompress(base64.b64decode(gz))
    with open(pymain, "wb") as f:
        f.write(bin)
    os.chmod(pymain, 0o775)