def canWinNim(n: int, stones: list):
    states = [False] * (n+1)
    for i in range(1, n+1):
        for step in stones:
            if not states[i-step] and i-step >= 0:
                states[i] = True
    return 'First' if states[-1] else 'Second'

N, K = tuple(map(int, input().split()))
stones = list(map(int, input().split()))
print(canWinNim(K, stones))