w = input()
count = 0
while True:
    t = input()
    if t == "END_OF_TEXT": break
    for c in t.lower().split(' '):
        if c == w: count += 1
print(int(count))