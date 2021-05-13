import math
N = int(input())

flag = False

for i in range(math.ceil(N/7)+1):
    for j in range(math.ceil(N/4)+1):
        if flag == True:
            continue
        #print(N - i * 7 - j * 4 )
        if N - i * 7 - j * 4 == 0:
            flag = True

if flag == True:
    print('Yes')
else:
    print('No')
