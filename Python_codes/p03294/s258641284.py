def lcm(a):
    from fractions import gcd
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

N = int(input())
S = list(map(int ,input().split()))
lcm_1 = lcm(S)-1
max_sum = 0
for i in range(N):
    max_sum += lcm_1%S[i]

print(max_sum)