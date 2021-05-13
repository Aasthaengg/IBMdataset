n = int(input())
bl = list(map(int,input().split()))

ans = []
for k in range(n):
    for i in range(n-1-k, -1, -1):
        if bl[i] == i+1:
            a = bl.pop(i)
            ans.append(a)
            break
    else:
        print(-1)
        exit()

for i in reversed(ans):
    print(i)