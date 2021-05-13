N, K = map(int, input().split())
d = list()
have = list()

for i in range(K):
    d.append(int(input()))
    holders = list(map(int, input().split()))
    for holder in holders:
        have.append(holder)
print(N - len(set(have)))
