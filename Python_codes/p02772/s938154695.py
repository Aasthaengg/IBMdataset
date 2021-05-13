N = int(input().rstrip())
l = [int(v) for v in input().rstrip().split()]
r = 'APPROVED'
for v in l:
    if v % 2 == 1:
        continue

    if v % 3 == 0 or v % 5 == 0:
        pass
    else:
        r = 'DENIED'
        break#
        
print(r)

