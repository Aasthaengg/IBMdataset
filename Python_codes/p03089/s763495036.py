N = int(input())
b = list(map(int, input().split()))

ans = []
while len(b) != 0:
    tmp = 0
    for i in range(1, len(b)+1):
        if b[i-1] == i:
            tmp = b[i-1]
    if tmp == 0:
        print(-1)
        exit()
    else:
        ans.append(tmp)
        del b[tmp-1]
        
for i in range(N-1, -1, -1):
    print(ans[i])