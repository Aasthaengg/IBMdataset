N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse = False)
cnt = 1


if 0 in A:
    print (0)
    exit()
else:
    for i in range(N):
        cnt *= A[i]
        if cnt > 10 ** 18:
            print (-1)
            exit ()
print (cnt)