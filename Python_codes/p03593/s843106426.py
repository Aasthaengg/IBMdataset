H,W = [int(x) for x in input().split()]
A = [input() for _ in range(H)]
char_cnts = [0]*26
for a in A:
    for c in a:
        char_cnts[ord(c)-97] += 1
if(H==1 or W==1):
    num_cnt1 = 0
    for i in char_cnts:
        if(i%2==1):
            num_cnt1 += 1
        if(num_cnt1>1):
            print('No')
            break
    else:
        print('Yes')

elif(H==2 and W==2):
    for i in char_cnts:
        if(i%4!=0):
            print('No')
            break
    else:
        print('Yes')
elif(H==2 or W==2):
    for i in char_cnts:
        if(i%2!=0):
            print('No')
            break
    else:
        print('Yes')
else:
    cnt = (H//2)*(W//2)
    for i in char_cnts:
        cnt -= i//4
        if(cnt<=0):
            print('Yes')
            break
    else:
        print('No')
