abc = list(map(int, input().split()))
abc.sort()
c = abc[2]
ab = abc[0] + abc[1]
if ab % 2 == 0:
    print((c * 2 - ab) // 2)
else:
    c += 1
    ab += 1
    print((c * 2 - ab) // 2 + 1)