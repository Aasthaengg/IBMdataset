n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ope = sum(b) - sum(a)
var = 0

for i in range(n):
    if a[i] >= b[i]:
        var += a[i] - b[i]
    else:
        var += (b[i] - a[i])%2
if (ope-var)%2 == 0 and ope >= var:
    print('Yes')
else:
    print('No')
