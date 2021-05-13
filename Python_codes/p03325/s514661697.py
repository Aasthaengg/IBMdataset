import sys

start = 0
for l in sys.stdin:
    if start == 0:
        start += 1
    else:
        list1 = list(map(int, l.split()))
        break
count = 0
for i in list1:
    while True:
        if i%2 == 0:
            count += 1
            i = i/2
        else:
            break
print(count)