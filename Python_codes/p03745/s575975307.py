n = int(input())
al = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
    
if al[1] > al[0]:
    now = 'U'
elif al[1] < al[0]:
    now = 'D'
else:
    now = 'E'

cnt = 1
for i in range(2, n):
    if now == 'U':
        if al[i] > al[i-1] or al[i] == 'E':
            now = 'U'
        elif al[i] < al[i-1]:
            cnt += 1
            i += 1
            now = 'E'
    elif now == 'D':
        if al[i] < al[i-1] or al[i] == 'E':
            now = 'D'
        elif al[i] > al[i-1]:
            cnt += 1
            now = 'E'
    elif now == 'E':
        if al[i] == al[i - 1]:
            now = 'E'
        elif al[i] > al[i - 1]:
            now = 'U'
        elif al[i] < al[i - 1]:
            now = 'D'
print(cnt)
