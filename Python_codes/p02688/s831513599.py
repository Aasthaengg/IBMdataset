N, K = map(int, input().split())

okashi_holders = set()

for _ in range(K):
    _ = input()
    for a in list(map(int, input().split())):
        okashi_holders.add(a)

print(N - len(okashi_holders))
