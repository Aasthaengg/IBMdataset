n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sub1 = 0
sub2 = 0

for i in range(n):
    if a[i] > b[i]:
        sub1 += a[i] - b[i]
    else:
        sub2 += (b[i] - a[i]) // 2

if sub1 <= sub2:
    print('Yes')
else:
    print('No')
