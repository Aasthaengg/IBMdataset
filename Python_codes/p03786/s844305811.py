n = int(input())
arr = list(map(int,input().split()))
arr.sort()

outs = -1
c = 0
for i in range(n-1):
    c += arr[i]
    if 2*c < arr[i+1]:
        outs = i

if outs >= 0:
    print(n - 1 - outs)
else:
    print(n)


