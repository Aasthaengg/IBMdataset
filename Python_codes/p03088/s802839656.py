def main():
    N = int(input())
    mod = 10**9 + 7
    v = {'TTTT': 1}
    for _ in range(N):
        u = {}
        for c, k in v.items():
            c = c[1:]
            for i in 'ACGT':
                t = c + i
                if 'AGC' in t or 'GAC' in t or 'ACG' in t or (t[0] == 'A' and t[2:] == 'GC') or (t[:2] == 'AG' and t[3] == 'C'):
                    continue
                u[t] = (u.get(t, 0) + k) % mod
        v = u
    print(sum(v.values()) % mod)

main()
