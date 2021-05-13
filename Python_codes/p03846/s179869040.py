N = int(input())

alist = list(map(int,input().split()))

alist.sort()

# print(alist)

mod = (10**9 + 7)

if N % 2 == 1:
    alist.pop(0)
    for i in range(N//2):
        # print('it', alist[i*2], 2*(i + 1), alist[i*2 + 1], 2*(i + 1))
        if alist[i*2] != 2*(i + 1) or alist[i*2 + 1] != 2*(i + 1):
            print(0)
            exit(0)
    print(2**(N//2)%mod)
else:
    for i in range(N//2):
        # print('it', alist[i*2], 2*(i + 1), alist[i*2 + 1], 2*(i + 1))
        if alist[i*2] != 2*i + 1 or alist[i*2 + 1] != 2*i + 1:
            print(0)
            exit(0)
    print(2**(N//2)%mod)
