N = int(input())
A = list(map(int,input().split()))
cnt1 = 0
cnt2 = 0
for i in A:
    if i % 2 == 1:
        cnt1 += 1
    elif i % 4 == 0:
        cnt2 += 1
if cnt1 + cnt2 == N:
    if cnt1 - 1 <= cnt2:
        print('Yes')
    else:
        print('No')
else:
    if cnt1 <= cnt2:
        print('Yes')
    else:
        print('No')