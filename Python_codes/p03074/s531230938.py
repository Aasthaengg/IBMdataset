N, K = map(int, input().split())
S = input()

#累積和の準備
zero_list = []
one_list = []
tmp = S[0]
count = 1
pin = 0
if tmp == '1':
    zero_list.append(0)
for i in range(1,N):
    if S[i] == tmp:
        count += 1
    else:
        if tmp == '1':
            one_list.append(count)
            count = 1
            tmp = '0'
        else:
            zero_list.append(count)
            count = 1
            tmp = '1'
if tmp == '1':
    one_list.append(count)
else:
    zero_list.append(count)
        
if K >= len(zero_list):
    pin =1
    print(N)
else:
    start = sum(zero_list[:K]) + sum(one_list[:K])
    ans = start
    if len(one_list) > K:
        tmp = start - zero_list[0] + zero_list[K] + one_list[K]
    else:
        tmp = start - zero_list[0] + zero_list[K]
    if tmp > ans:
        ans = tmp
    basyo = 1
    last = len(one_list)
    while basyo + K < last:
        tmp = tmp -zero_list[basyo] - one_list[basyo -1] + zero_list[K + basyo] + one_list[K + basyo]
        if tmp > ans:
            ans = tmp
        basyo += 1
    if len(one_list) != len(zero_list) and K + basyo <  len(zero_list):
        tmp = tmp -zero_list[basyo] - one_list[basyo -1] + zero_list[K + basyo] 
        if ans < tmp:
            ans = tmp
if pin == 0:
    print(ans)