n = int(input()); a = list(map(int, input().split())); b = -1; x = 1
for i in range(n-1):
    if b == 0:
        if a[i] > a[i+1]: b = -1; x += 1
    elif b == 1:
        if a[i] < a[i+1]: b = -1; x += 1
    else:
        if a[i] < a[i+1]: b = 0
        elif a[i] > a[i+1]: b = 1
print(x)