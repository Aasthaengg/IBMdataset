N = int(input())

four = 0

while 4*four <= N:
    X = N - 4*four
    if X % 7 == 0:
        print("Yes")
        exit()
    four += 1

print("No")