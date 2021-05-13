N = int(input())
a = [int(input()) for _ in range(N)]

for i in range(N):
    if a[i] % 2 == 1:
        print('first')
        exit()
print('second')