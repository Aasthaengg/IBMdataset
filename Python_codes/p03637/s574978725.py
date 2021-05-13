n = int(input())
a = list(map(int, input().split()))
o_cnt=0
t2_cnt=0
t4_cnt=0
for i in a:
    if i%2==1:
        o_cnt += 1
    elif i%4==0:
        t4_cnt += 1
    else:
        t2_cnt += 1

if t4_cnt > 0:
    if t4_cnt >= (o_cnt-n%2):
        print('Yes')
    else:
        print('No')
else:
    if t2_cnt==n:
        print('Yes')
    else:
        print('No')