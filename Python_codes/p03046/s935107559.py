M, K = map(int, input().split())

max_val = 2 ** M

ans = []
if K < max_val:
    if M == 0:
        ans = [0, 0]
    elif M == 1:
        if K == 0:
            ans = [0, 0, 1, 1]
        else:
            ans = [-1]
    else:
        for i in range(max_val):
            if i != K:
                ans.append(i)
        ans.append(K)
        for i in range(max_val-1, -1, -1):
            if i != K:
                ans.append(i)
        ans.append(K)
else:
    ans = [-1]
print(*ans)
