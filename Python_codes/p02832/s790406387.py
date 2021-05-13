N = int(input())
a = list(map(int,input().split()))

bcnt = 0
signal = 1

for i in a:
    if i == signal:
        signal += 1
    else:
        bcnt += 1

if bcnt == N:
    print('-1')
else:
    print(bcnt)