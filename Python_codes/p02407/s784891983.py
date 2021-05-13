n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1,-1,-1):
    if i == 0:
        print(a[i])
    else:
        print(a[i],end=" ")