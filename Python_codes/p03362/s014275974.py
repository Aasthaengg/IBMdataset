import math
N = int(input())

def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    data = [i + 1 for i in range(2, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]
    return prime + data

prime_list = get_prime(55555)
ans_list = []
for i in prime_list:
    if i % 5 == 1:
        ans_list.append(i)
    if len(ans_list) == N:
        break
for i in ans_list:
    print(i, end=' ')