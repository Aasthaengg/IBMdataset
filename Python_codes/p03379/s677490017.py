n = int(input())
x = list(map(int,input().split()))

lis = sorted(x)
median = lis[int(n/2)]
median2 = lis[int((n-2)/2)]

for i in range(n):
    if x[i] < median:
        print(median)
    else:
        print(median2)