n = list(map(int, input().split()))
print('Yes' if sum(n) % 9 == 0 else 'No')