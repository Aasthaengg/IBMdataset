N = int(input())
a = list(int(input()) for i in range(N))

if all(a[i] % 2 == 0 for i in range(N)):
    print('second')
else:
    print('first')