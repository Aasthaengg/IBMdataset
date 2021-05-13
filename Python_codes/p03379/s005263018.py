import copy
n = int(input())
X = [0]+[int(i) for i in input().split()]
Copy = copy.deepcopy(X)

X.sort()
index_right = int(n/2+1)
index_left = index_right-1
key_r = X[index_right]
key_l = X[index_left]

for i in range(1,n+1):
    if Copy[i] <= key_l:
        print(key_r)
    else:
        print(key_l)