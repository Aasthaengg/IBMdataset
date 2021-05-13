N = input()
N = int(N)
array = list(map(int,  input().split()))
cnt = 0
for i in range(N):
    # print(' '.join(map(str, array)))
    for j in range(N-1, i, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            cnt += 1
print(' '.join(map(str, array)))
print("%d" % (cnt))
