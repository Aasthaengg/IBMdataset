n = int(input())
hl = list(map(int, input().split()))

curr = hl[0]-1
for i in range(1,n):
    if hl[i] > curr:
        curr = hl[i]-1
    elif hl[i] == curr:
        pass
    else:
        print('No')
        break
else:
    print('Yes')