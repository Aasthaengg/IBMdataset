n = int(input())
b = list(map(int, input().split()))

ans = []
while len(b) > 0:
    ind = -1
    for i in range(len(b)):
        if b[i] == i + 1:
            ind = i
    if ind == -1:
        break
    else:
        ans.append(b.pop(ind))
    
if ind == -1:
    print(-1)
else:
    print(*ans[::-1], sep='\n')