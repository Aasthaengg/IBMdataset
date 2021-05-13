a = list(map(int,input().split()))
A = a[0]
B = a[1]
C = a[2]
aa = input()
K = int(aa)

flag = 0
r = 0

while r <= K:
    if A < B:
        if B < C:
            flag = 1
            break
        else:
            C = C*2
            r = r + 1
    else:
        B = B*2
        r = r + 1
if flag == 0:
    print('No')
else:
    print('Yes')
