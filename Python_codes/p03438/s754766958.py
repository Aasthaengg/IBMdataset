N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ac = 0
bc = 0
for i in range(N):
    if a[i] < b[i]:
        ac += (b[i] - a[i]) // 2
    else:
        bc += a[i] - b[i]
if ac >= bc:
    print('Yes')
else:
    print('No')
