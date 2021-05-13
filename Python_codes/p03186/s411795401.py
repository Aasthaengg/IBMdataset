A, B, C = map(int, input().rstrip().split(' '))

count = B
if A + B >= C:
    count += C
else:
    count +=  A + B + 1

print(count)