import numpy as np

n = int(input())
A = list(map(int,input().split()))

cnt = np.sum(np.where(np.array(A) < 0, True, False))

#print(cnt)

A = list(map(lambda x:abs(x), A))


if cnt%2 == 0:
    print(sum(A))
else:
    print(sum(A)-2*min(A))