N = int(input())
N1 = N // 10
if N % 2 == 1:
    print(0)
else:
    counter = 0
    div = 10
    while True:
        num = N // div
        if num == 0:
            break
        counter += num
        div *= 5
    print(counter)