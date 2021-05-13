a = list(map(int, input().split()))
rec1 = int(a[0]* a[1])
rec2 = int(a[2] * a[3])

if rec1 > rec2:
    result = rec1
elif rec2 > rec1:
    result = rec2
else:
    result = rec1

print(result)