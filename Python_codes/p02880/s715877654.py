N = int(input())

flag = False
for i in range(9, 0, -1):
    q, r = divmod(N, i)
    if r == 0 and q < 10:
        flag = True
            
if flag:
    print('Yes')
else :
    print('No')