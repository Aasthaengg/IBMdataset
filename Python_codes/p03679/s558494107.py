X, A, B = list(map(int,input().split()))
print('delicious' if -A+B <= 0 else 'safe' if B-A <= X else 'dangerous')