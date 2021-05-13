N = int(input())
B = list(map(int, input().split()))

ans = []
while B:
    flag = False
    idx = -1
    for i in range(len(B)):
        if B[i] == i+1:
            flag = True
            idx = i
    else:
        if flag:
            ans.append(B[idx])
            B.pop(idx)
        else:
            print(-1)
            exit(0)

for i in reversed(range(N)):
    print(ans[i])
