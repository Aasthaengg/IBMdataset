n = int(input())
b = list(map (int, input().split()))

ans = []
while b != []:
    flag = True
    for i in range(len(b)-1, -1, -1):
        if b[i]-i-1 == 0:
            flag = False
            ans.append(b.pop(i))
            break
    if flag:
        print(-1)
        exit()
for i in range(n-1, -1, -1):
    print(ans[i])
