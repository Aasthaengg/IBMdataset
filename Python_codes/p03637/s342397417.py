N, *A = map(int, open(0).read().split())
cnt1 = cnt2 = cnt4 = 0
for a in A:
    if a % 4 == 0:
        cnt4 += 1
    elif a % 2 == 0:
        cnt2 += 1
    else:
        cnt1 += 1

if cnt4 >= cnt1:
    print('Yes')
elif cnt4 == cnt1-1 and cnt2 == 0:
    print('Yes')
else:
    print('No')