N = int(input())
a = list(map(int,input().split()))
count = 0
count2 = 0
for i in a:
    if i%4==0:
        count += 1
    elif i%2==0:
        count2 += 1
if count2 != 0:
    if (N-count2)%2 != 0:
        value = (N-count2)//2
    else:
        value = (N-count2)//2-1
else:
    if count >= N//2:
        value = N//2-1
    else:
        value = N//2

    value = N//2-1

if count > value:
    print('Yes')
else:
    print('No')

1414
414
