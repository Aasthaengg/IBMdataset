N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

operation = sum(B) - sum(A)

cntp = 0
cntn = 0
for a, b in zip(A, B):
    c = b - a
    if c > 0:
        cntp += c
        if c % 2 != 0:
            operation -= 1
    elif c < 0:
        cntn += -c


if operation >= cntn:
    print('Yes')
else:
    print('No')