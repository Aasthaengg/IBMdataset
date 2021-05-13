
N = int(input())
B = list(map(int, input().split()))

ans = []
removed = [False] * N

flag = True
while flag:
    flag = False
    
    idx_remove = -1
    idx = 0
    for i in range(N):
        if removed[i]:
            continue

        if idx + 1 == B[i]:
            idx += 1
            idx_remove = i

        else:
            idx += 1
    
    if idx_remove != -1:
        ans.append(B[idx_remove])
        removed[idx_remove] = True
        flag = True


if all(removed):
    for a in ans[::-1]:
        print(a)
else:
    print(-1)