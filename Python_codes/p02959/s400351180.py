N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
count = sum(a)

for i in range(N):
    if a[i] >= b[i]:
        a[i] -= b[i]
        b[i] = 0
    else:
        b[i] -= a[i]
        a[i] = 0
        if a[i+1] > b[i]:
            a[i+1] -= b[i]
            b[i] = 0
        else:
            b[i] -= a[i+1]
            a[i+1] = 0
print(count-sum(a))        
