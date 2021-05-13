N = int(input())
S = input()

l_blacks = 0
r_whites = 0

for c in S:
    if c == '.':
        r_whites += 1

mins = r_whites
for c in S:
    if c == '.':
        r_whites -= 1
    if c == '#':
        l_blacks += 1
    mins = min(mins, r_whites + l_blacks)
print(mins)