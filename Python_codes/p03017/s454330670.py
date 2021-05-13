n,a,b,c,d = map(int, input().split())
s = str(input())

a,b,c,d = a-1,b-1,c-1,d-1

cnt = 0
for i in range(a,max(c,d)+1):
    if s[i] == '#':
        cnt += 1
        if cnt >= 2:
            print('No')
            exit()
    else:
        cnt = 0

cnt = 0
if b >= 2:
    if s[b-2] == '.' and s[b-1] == '.':
        cnt = 2

if s[b-1] == '.':
    cnt = 1

if c > d:
    if s[d-1] == '.' and s[d+1] == '.':
        print('Yes')
        exit() 
    for i in range(b,d+1):
        if s[i] == '.':
            cnt += 1
            if cnt >= 3:
                print('Yes')
                exit()
        else:
            cnt = 0
        if i == d:
            print('No')
            exit()
else:
    print('Yes')

