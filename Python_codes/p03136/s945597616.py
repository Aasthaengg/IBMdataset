n = int(input())
l = list(map(int,input().split()))
flg = 0
for i in range(0, n):
    if l[i] < sum(l)-l[i]:
        pass
    else:
        flg = 1
if flg == 1:
    print('No')
else:
    print('Yes')