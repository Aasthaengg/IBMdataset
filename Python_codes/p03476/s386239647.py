Q = int(input())
A = []
B = []
for i in range(Q):
    in1, in2 = list(map(int,input().split()))
    A.append(in1)
    B.append(in2)
    
def sieve(N):
    p = 0
    prime = []
    is_prime = [1 for _ in range(N + 1)]
    is_prime[0], is_prime[1] = 0, 0
    for i in range(2, N + 1):
        if is_prime[i]:
            p += 1
            temp = i
            prime.append(i)
            while(temp <= N):
                is_prime[temp] = 0
                temp += i
            is_prime[i] = 1
    return is_prime

p_list = sieve(10 ** 5 + 10)
acc = [0, 0]
for i in range(3, 10 ** 5 + 1, 2):
    if p_list[i] and p_list[(i + 1) // 2]:
        acc.append(acc[-1] + 1)
    else:
        acc.append(acc[-1])
for i in range(Q):
    print(acc[(B[i] + 1) // 2] - acc[(A[i] + 1) // 2 - 1])