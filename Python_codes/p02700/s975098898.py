def resolve():
    A, B, C, D = list(map(int, input().split()))
    import math
    n_taka_attacks = math.ceil(C/B)
    n_ao_attacks = math.ceil(A/D)
    print("Yes" if n_taka_attacks <= n_ao_attacks else "No")


if '__main__' == __name__:
    resolve()