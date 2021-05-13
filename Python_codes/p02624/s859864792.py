def generate_divisor_count_sieve(N):
    tau = [0]*(N+1)
    for d in range(1,N+1):
        for n in range(d,N+1,d):
            tau[n] += 1
    return tau
N = int(input())
tau = generate_divisor_count_sieve(N)
print(sum([n*tau[n] for n in range(1,N+1)]))