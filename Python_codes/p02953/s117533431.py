n = int(input())
h =list(map(int, input().split()))

if n==1:
    print('Yes')
    exit(0)
if n==2:
    if h[0] >= h[1]-1:
        print('Yes')
        exit(0)
    else:
        print('No')
        exit(0)

h[0] -=1

for i in range(1, n-1):
    if h[i-1] == h[i] and h[i] <=h[i+1]:
        continue
    elif h[i-1] == h[i] and h[i] >h[i+1]:
        print('No')
        exit(0)

    elif h[i] <= h [i+1]+1:
        h[i] -= 1
    elif h[i] > h [i+1]+1:
        print('No')
        exit(0)


print('Yes')