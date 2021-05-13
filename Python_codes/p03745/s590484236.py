num = int(input())
seq = list(map(int, input().split()))

prev = None
increase = None
count = 0

prev = seq[0]
for x in seq[1:]:
    if increase is True:
        if x >= prev:
            pass
        else:
            increase = None
            count += 1
    elif increase is False:
        if x <= prev:
            pass
        else:
            increase = None
            count += 1
    elif increase is None:
        if x == prev:
            pass
        elif x > prev:
            increase = True
        else:
            increase = False
    prev = x

count += 1
print(count)
