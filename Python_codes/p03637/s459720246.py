n = int(input())
a_list = list(map(int,input().split()))
cntn = 0
cnt2 = 0
cnt4 = 0
for i in a_list:
    if i%4 == 0:
        cnt4 += 1
    elif i%2 == 0:
        cnt2 += 1
    else:
        cntn += 1
        
flag = True

if cnt4+ 1 >= cntn :
    flag = True

else:
    flag = False

if cnt2 >= 1:
    if cnt4 >= cntn :
        flag = True
    else:
        flag = False

if flag:
    print('Yes')

else:
    print('No')