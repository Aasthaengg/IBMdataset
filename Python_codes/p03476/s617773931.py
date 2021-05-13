n = int(input())

def sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

prime = sieve_of_eratosthenes(10**5 + 1)

numlike2017 = [0 for i in range(10**5 + 1)]
for i in prime:
    if (i+1)//2 in prime:
        numlike2017[i] = 1

def cumulative_sum(collection):
    result = [collection.pop(0)]
    for item in collection:
        result.append(result[-1] + item)
    return result
cs2017 = cumulative_sum(numlike2017)

ans = []
for i in range(n):
    a, b = map(int, input().split())
    ans.append(cs2017[b] - cs2017[a-1])

for i in ans:
    print(i , flush=True)
