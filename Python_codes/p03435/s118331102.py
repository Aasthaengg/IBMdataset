import sys

c = [input().split() for i in range(3)]
num = [int(c[i][j]) for i in range(3) for j in range(3)]

if num[0] + num[4] != num[1] + num[3]:
    print('No')
    sys.exit()
elif num[4] + num[8] != num[5] + num[7]:
    print('No')
    sys.exit()
elif num[0] + num[8] != num[2] + num[6]:
    print('No')
    sys.exit()

print('Yes')