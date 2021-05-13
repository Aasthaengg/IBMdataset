n = int(input().strip())
if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    lst = [0 for i in range(0,n+1)]
    lst[0] = 1
    lst[1] = 1
    for i in range(0,n-1):
        lst[i+2] = lst[i+1] + lst[i]
    print(lst[n])
