N = int(input())
As = list(map(int,input().split()))
zoka = 0
before = As[0]
c = 1
for i in range(1,N):
    if before < As[i]:
        if zoka == 0 or zoka == 1:
            zoka = 1
        else:
            c+=1
            zoka = 0
        before = As[i]
    elif before > As[i]:
        if zoka == 0 or zoka == 2:
            zoka = 2
        else:
            c+=1
            zoka = 0
        before = As[i]
print(c)
