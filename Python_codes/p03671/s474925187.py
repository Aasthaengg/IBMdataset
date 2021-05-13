import sys
array_abc = list(map(int,input().split()))
if min(array_abc) < 0 or max(array_abc) > 10000:
    sys.exit()

min = 30000
for I in range(len(array_abc)):
    for J in range(len(array_abc)):
        if not I == J:
            if min > array_abc[I] + array_abc[J]:
                min = array_abc[I] + array_abc[J]

print(min)
