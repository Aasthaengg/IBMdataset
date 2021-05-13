N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = sum(a)
B = sum(b)
sa = []
num = B-A
flag = True
for i in range(N):
    sa.append(b[i]-a[i])
    if a[i] != b[i]:
        flag= False
if flag:
    print('Yes')
else:
    if num <= 0:
        print('No')
    else:
        cnt = 0
        for i in range(N):
            if sa[i] > 0:
                cnt += sa[i]-sa[i]//2
        if cnt <= num:
            print('Yes')
        else:
            print('No')