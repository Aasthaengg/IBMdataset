n = int(input())
s = input()
r, b = 0, 0
for _ in s:
    if(_ == 'R'):
        r += 1
    else:
        b += 1
print('Yes' if r > b else 'No')