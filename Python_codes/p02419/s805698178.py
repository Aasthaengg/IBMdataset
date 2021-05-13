taisho = input().lower()

count = 0

while True:
    w = input()
    if w == 'END_OF_TEXT':
        break
    for x in w.lower().split(' '):
        if taisho == x:
            count += 1

print(count)

