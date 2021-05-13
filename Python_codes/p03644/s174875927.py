N = int(input())
for i in [2**x for x in range(0, 9)]:
    if i <= N:
        r = i
print(r)
