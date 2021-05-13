n,k = map(int,input().split())
a = list(map(int,input().split()))

sum = 0

for i in range(0,k):
        sum += a[i]

was = sum
for i in range(n-k):
        now=was - a[i] + a[k+i]
        if was < now:
                print('Yes')
        else:
                print('No')
        was = now