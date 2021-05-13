A,B = list(map(int, input().split()))

x = 0

for i in range(2):
    if A <= B:
        x = x + B
        B -= 1
    else:
        x = x + A
        A -= 1

print(x)