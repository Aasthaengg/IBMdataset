n = int(input())
a = list(map(int, input().split()))

left = []
right = []

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            right.append(a[i])
        else:
            left.append(a[i])
    
    print(*(left[::-1]+right))
else:
    for i in range(n):
        if i % 2 == 0:
            left.append(a[i])
        else:
            right.append(a[i])
    
    print(*(left[::-1]+right))