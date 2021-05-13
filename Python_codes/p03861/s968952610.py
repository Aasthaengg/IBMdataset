a, b, x = map(int, input().split())
print(b // x - max(0, a - 1) // x +
      (1 if a == 0 else 0))  # aが0のときどうすりゃいいのか直感ではまったくわからんのだが
