l = input().split()
N = int(l[0])
K = int(l[1])

# print(N, K)

if K == 1:
    print(0)
    exit()

remain = N - K
print(remain)
