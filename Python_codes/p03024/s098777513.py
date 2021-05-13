S = input()
o = S.count('o')
x = S.count('x')
o += 15 - o - x
print("YES" if o >= 8 else "NO")