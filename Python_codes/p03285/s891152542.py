import math
N = int(input())

flag = False

for i in range(100):
    for j in range(100):
        if flag == True:
            continue
        #print(N - i * 7 - j * 4 )
        if N - i * 7 - j * 4 == 0:
            flag = True

if flag == True:
    print('Yes')
else:
    print('No')
