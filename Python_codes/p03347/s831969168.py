n = int(input())
a = [int(input()) for _ in range(n)]
if any(a[i] > i for i in range(n)):
    print(-1)
    exit()
a = a[::-1]

cnt = 0
tmp = 0
for i in range(n):
    if a[i] > tmp:
        tmp = a[i]
        cnt += tmp


    elif a[i] < tmp:
        print(-1)
        exit()

    tmp -= 1

print(cnt)