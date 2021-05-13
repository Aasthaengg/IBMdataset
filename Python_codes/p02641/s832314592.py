import numpy as np
def forbidden_list():
    X, N = map(int,input().split())
    p = list(map(int, input().split()))
    lis = np.array([1 for i in range(102)])
    lis[p] = 0
    index = X
    ma = 102 - X
    for i in range(max(X,ma)):
        if index - i >= 0 and lis[index-i]:
            print(index-i)
            break
        elif index + i <= 101 and lis[index + i]:
            print(index + i)
            break
    
forbidden_list()