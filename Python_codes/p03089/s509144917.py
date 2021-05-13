N = int(input())
b = list(map(int,input().split()))
i = N-1
jun = []
while i > -1:
    if b[i] == i+1:
        del b[i]
        jun.append(i+1)
        i = len(b)-1
    else:
        i -= 1
if len(b) != 0:
    print(-1)
else:
    for j in jun[::-1]:
        print(j)