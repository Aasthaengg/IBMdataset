n = int(input())
h = list(map(int,input().split()))
tmp = h[0]
isOK = True
for i in range(1,n):
    #print(tmp,h[i])
    if tmp < h[i]:
        tmp = h[i] - 1
    elif tmp == h[i]:
        tmp = h[i]
    else:
        isOK = False
        break
if isOK:
    print('Yes')
else:
    print('No')