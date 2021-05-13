X = int(input())
answer = (1001,1001)
for A in range(-1000, 1000):
    for B in range(-1000, 1000):
        if A ** 5 - B ** 5 == X:
            answer = (A, B)
            break
    if answer[0] != 1001:
        break
print(' '.join(map(str, answer)))