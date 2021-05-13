N = int(input())
apple = [int(input()) for _ in range(N)]
for i in apple:
    if i % 2 == 1:
        print('first')
        exit()
print('second')