N = int(input())

if N%2==1:
    print(0)
else:
    i = 10
    count = 0
    while i <= N:
        count += N//i
        i = i*5

    print(count)
