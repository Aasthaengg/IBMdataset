n,k,q = map(int, input().split())
p = [k-q]*n
for i in range(q):
    a = int(input())
    p[a-1] += 1
for j in p:
    if 0 < j:
        print('Yes')
    else:
        print('No')