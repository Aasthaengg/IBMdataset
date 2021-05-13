M, K = map(int,input().split())
if M == 1 and K == 1:
    print(-1)
elif K == 0:
    for i in range(2**M):
        print(i,end=" ")
        print(i,end=" ")
elif 2**M <= K:
    print(-1)
else:
    for i in range(2**M):
        if i != K:
            print(i,end=" ")
    print(K, end=" ")
    for i in reversed(range(2**M)):
        if i != K:
            print(i,end=" ")
    print(K, end=" ")