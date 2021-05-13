
M,K = map(int,input().split())

if K >= 2 ** M:
    print (-1)

elif M == 1 and K == 0:
    print ("0 0 1 1")

elif M == 1 and K == 1:
    print ("-1")

else:
    ans = []

    for i in range(2 ** M):
        if i != K:
            ans.append(i)

    ans.append(K)

    for i in range(2 ** M):
        if 2 ** M - i - 1 != K:
            ans.append(2 ** M - i - 1)

    ans.append(K)

    print (" ".join(map(str,ans)))
