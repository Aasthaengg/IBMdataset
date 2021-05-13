n, k = map(int, (input().split()))
s = input()

c = sum([s[i:i + 2] in ('LR', 'RL') for i in range(n - 1)])

print(n - c - 1 + int(min(c / 2, k) * 2))