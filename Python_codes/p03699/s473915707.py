import sys
N = int(input())

num = sorted([int(input()) for i in range(N)])
MAX = sum(num)

if MAX % 10 != 0:
    print(MAX)
    sys.exit()
else:
    for i in range(N):
        if num[i] % 10 != 0:
            print(MAX - num[i])
            sys.exit()

print(0)
