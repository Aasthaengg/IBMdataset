N = int(input())

for i in range(1,10):
    mod = N % i
    c = N // i
    if mod == 0 and c <= 9:
        print('Yes')
        exit()
else:
    print('No')