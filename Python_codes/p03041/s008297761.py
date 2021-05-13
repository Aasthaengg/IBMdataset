N, K = map(int, input().split())
S = input()

list = [s for s in S]

list[K - 1] = list[K - 1].lower()

print(''.join(list))
