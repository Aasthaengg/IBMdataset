M, K = map(int, input().split())
if 2**M <= K:
    print("-1")
else:
    if M == 0:
        if K == 0:
            print("0 0")
        else:
            print("-1")
    elif M == 1:
        if K == 0:
            print("0 0 1 1")
        else:
            print("-1")
    else:
        ret = ""
        for i in range(2**M):
            if i != K:
                ret += str(i)+" "
        ret += str(K) + " "
        for i in range(2**M-1, -1, -1):
            if i != K:
                ret += str(i)+" "
        ret += str(K)
        print(ret)