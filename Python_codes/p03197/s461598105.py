N = int(input())
A = [int(input()) for _ in range(N)]

cnt = 0
for a in A:
    if a % 2 == 1:
        print('first')
        exit()
        
print('second')