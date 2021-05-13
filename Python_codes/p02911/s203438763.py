n,k,q = map(int,input().split())
a = list(int(input()) for i in range(q))
z = [0] * n
for i in range(q):
    z[a[i]-1] += 1
for i in range(n):
    if z[i] >= q - k + 1:
        print('Yes')
    else:
        print('No')