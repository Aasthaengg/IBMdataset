abc = [int(i) for i in input().split()]
abc.sort()
ab, bc = abc[2] - abc[1], abc[2] - abc[0]
cnt = 0
if ab % 2 == 0 and bc % 2 == 0:
    cnt += ab//2
    cnt += bc//2
elif ab % 2 != 0 and bc % 2 != 0:
    cnt += ab//2
    cnt += bc//2 + 1
else:
    cnt += ab//2
    cnt += bc//2 + 2
print(cnt)