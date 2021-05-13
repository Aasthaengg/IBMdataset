N = int(input())
A = [0]*(1000001)
for a in list(map(int, input().split())):
    A[a] += 1

# MFPF = Most Frequent Prime Factor
MFPF_n = 0
seen_prime_factor = [0]*(1000001)
for i in range(2, 1000001):
    if seen_prime_factor[i]:
        continue
    n = i
    tmp = 0
    while n < 1000001:
        tmp += A[n]
        seen_prime_factor[n] = 1
        n += i
    MFPF_n = max(MFPF_n, tmp)

if MFPF_n < 2:
    print('pairwise coprime')
elif MFPF_n - A[1] < N:
    print('setwise coprime')
else:
    print('not coprime')