N=int(input())
H=list(map(int, input().split()))

m = 0
f = 0
for h in H:
    m = max(m, h)
    if m > h+1:
        print('No')
        f = 1
        break
if not f:
    print('Yes')
