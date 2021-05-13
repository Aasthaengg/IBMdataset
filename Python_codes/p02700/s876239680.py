A, B, C, D = list(map(int, input().split()))

win = ''

while True:
    C = C - B
    if C <= 0:
        win = 'Yes'
        break

    A = A - D
    if A <= 0:
        win = 'No'
        break
print(win)