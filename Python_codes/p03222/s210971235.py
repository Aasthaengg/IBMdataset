import sys
MOD = 1000000007


def main():
    h, w, k = [int(x) for x in input().split()]
    fibonacci = [1, 2]
    for i in range(w - 2):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    pattern = [0 for _ in range(w)]
    pattern[0] = 1
    for _ in range(h):
        nextp = [0 for _ in range(w)]
        for i in range(w):
            nextp[i] = (pattern[i] * (fibonacci[max(0, i - 1)] * fibonacci[max(0, w - (i + 2))])) % MOD
            if i > 0:
                nextp[i] += (pattern[i - 1] * (fibonacci[max(0, i - 2)] * fibonacci[max(0, w - (i + 2))])) % MOD
            if i < w - 1:
                nextp[i] += (pattern[i + 1] * (fibonacci[max(0, i - 1)] * fibonacci[max(0, w - (i + 3))])) % MOD
            nextp[i] %= MOD
        pattern = nextp
    print(pattern[k-1])


main()
