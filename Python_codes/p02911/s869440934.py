n, k, q = map(int, input().split())

res= [0]*n
for _ in range(q):
    a = int(input())
    res[a-1] += 1

for i in range(n):
    if k-q+res[i] <=0:
        print('No')
    else:
        print('Yes')