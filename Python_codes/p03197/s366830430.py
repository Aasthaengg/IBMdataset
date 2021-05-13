N = int(input())
a = [int(input()) for _ in range(N)]

for i in range(N) :
    if a[i] % 2 != 0 :
        print('first')
        break
else :
    print('second')