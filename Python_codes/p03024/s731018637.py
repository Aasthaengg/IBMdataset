S = input()
k = len(S)
win = S.count('o')
print("YES" if (15-k) >= (8-win) else "NO")