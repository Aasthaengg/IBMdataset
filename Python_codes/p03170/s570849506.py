
N,K = map(int,input().split())

a = list(map(int,input().split()))

gr = [0] * (K+1)

for i in range(K+1):

    mex = [0] * (N+1)
    for j in a:
        if i-j >= 0:
            mex[gr[i-j]] = 1

    for k in range(N+1):
        if mex[k] == 0:
            gr[i] = k
            break

if gr[-1] == 0:
    print ("Second")
else:
    print ("First")
