o = input()
e = input()

for (a, b) in zip(o, e):
    print(f'{a}{b}', end='')
if len(o) > len(e):
    print(o[-1], end='')
print()
