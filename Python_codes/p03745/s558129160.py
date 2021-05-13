_ = input()
A = map(int, input().split())
prev = next(A)
up = None
count = 1
for i in A:
    if prev < i:
        if up is None:
            up = True
        elif not up:
            count += 1
            up = None
    elif prev > i:
        if up is None:
            up = False
        elif up:
            count += 1
            up = None
    prev = i
print(count)
