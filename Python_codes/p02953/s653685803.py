N, *A = map(int, open(0).read().split())
pre = A[-1]
for i in range(N-1, -1, -1):
    a = A[i]
    if pre < a-1:
        print('No')
        exit()
    elif pre < a:
        pre = a-1
    else:
        pre = a
print('Yes')