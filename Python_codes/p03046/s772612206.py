M, K = map(int, input().split())

if K == 0:
    for i in range(pow(2, M + 1)//2):
        print (i, i, end = '')
        if i != pow(2, M + 1)//2 - 1:
            print (' ', end = '')
    exit()

tmp = 0
for i in range(pow(2, M)):
    tmp ^= i

if K >= pow(2, M):
    print (-1)
    exit()

if tmp ^ K != K:
    print (-1)
    exit()
    
#出力部分
print (K, end = ' ')
for i in range(pow(2, M) - 1, -1, -1):
    if i != K:
        print (i, end = ' ')
print (K, end = ' ')
for i in range(pow(2, M)):
    if i != K:
        print (i, end = '')
        if K == pow(2, M) - 1:
            if i != pow(2, M) - 2:
                print (end = ' ')
        else:
            if i != pow(2, M) - 1:
                print (end = ' ')

