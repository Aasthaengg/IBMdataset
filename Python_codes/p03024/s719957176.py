S = input()
rest = 15
win = 0
for c in S:
    if c == 'o':
        win += 1
    rest -= 1
if win + rest >= 8:
    print("YES")
else:
    print("NO")