N = int(input())
K = int(input())

num = 1
for i in range(N):
    if (num * 2) - num < K:
        num = num * 2
    else :
        num += K

print(num)