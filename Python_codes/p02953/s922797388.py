n = int(input())
h = list(map(int,input().split()))
j = h[0]

for i in range(1,n):
    if h[i] > j:
        h[i] -= 1
        j = h[i]
    else:
        pass

l = list(h)
l.sort()
if h == l:
    print('Yes')
else:
    print('No')