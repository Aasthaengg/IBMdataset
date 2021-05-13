import sys

input = sys.stdin.readline().strip('\n')
flag = 0
for idx in range(len(input)):
    if input[idx] != 'h' and input[idx] != 'i':
        print('No')
        flag = -1
        break
    elif input[idx] == 'h':
        if idx == len(input)-1:
            print('No')
            flag = -1
            break
        elif input[idx+1] != 'i':
            print('No')
            flag = -1
            break
    else:
        if idx == 0:
            print('No')
            flag = -1
            break
        elif input[idx-1] != 'h':
            print('No')
            flag = -1
            break

if flag == 0:
    print('Yes')
