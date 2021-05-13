n,k,q = map(int,input().split())
nlist = [0]*n
for i in range(q):
    a = int(input())
    nlist[a-1] += 1
for i in range(n):
    if q - nlist[i] >= k:
        print('No')
    else:
        print('Yes')