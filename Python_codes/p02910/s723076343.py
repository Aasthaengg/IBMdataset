s = input()
playable = True
for i, c in enumerate(s):
    if i % 2 == 1 and c == 'R' or i % 2 == 0 and c == 'L':
        playable = False
        break
print("Yes" if playable else "No")