n = int(input())
h = list(map(int,input().split()))
for i in range(1,n):
    if h[i] > h[i-1]:
        h[i] -= 1
    else:
        pass
l = list(h)
l.sort()
if h == l:
    print('Yes')
else:
    print('No')