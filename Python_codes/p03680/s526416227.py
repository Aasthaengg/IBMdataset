N = int(input())
a = [int(input()) for _ in range(N)]
count = 1
num = a[0]

while count <= N:
    if num != 2:
        num = a[num-1]
        count += 1
    else:
        print(count)
        exit()
print(-1)