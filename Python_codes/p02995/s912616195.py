from math import gcd


def count_indivs(N):
    return N - (N // C + N // D - N // L)


A, B, C, D = map(int, input().split())
L = C * D // gcd(C, D)
print(count_indivs(B) - count_indivs(A - 1))
