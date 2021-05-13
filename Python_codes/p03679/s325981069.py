X, A, B = list(map(int, input().split()))
print('delicious' if B<=A else 'safe' if B<=A+X else 'dangerous')