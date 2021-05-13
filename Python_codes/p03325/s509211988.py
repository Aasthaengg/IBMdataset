N = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if a[i]%2 == 1:
        continue
    else:
        while True:
            if a[i]%2 == 1:
                break
            else:
                a[i] //= 2
                cnt += 1
print(cnt)