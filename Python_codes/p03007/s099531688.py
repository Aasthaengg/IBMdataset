N = int(input())
A = list(map(int, input().split()))
A.sort()

neg = [n for n in A if n < 0]
pos = [n for n in A if n >= 0]

if len(neg) == 0:  # all positive
    x = A.pop(0)
    print(sum(A) - x)
    pivot = A.pop()
    for y in A:
        print(x, y)
        x -= y
    print(pivot, x)
elif len(pos) == 0:  # all negative
    x = A.pop()
    print(x - sum(A))
    for y in A:
        print(x, y)
        x -= y
else:
    print(sum(pos) - sum(neg))
    pivot = pos.pop()
    x = neg.pop()
    for y in pos:
        print(x, y)
        x -= y
    x, pivot = pivot, x
    for y in neg:
        print(x, y)
        x -= y
    print(x, pivot)
