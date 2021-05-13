N = int(input())
a = list(map(int, input().split()))

count = 0

for x in range(N):
    if x != N - 1:
        if a[x] == a[x + 1]:
            if x < N - 2:
                if a[x + 2] == 10000:
                    a[x + 1] = 9999
                    count += 1
                else:
                    a[x + 1] = 10000
                    count += 1
            else:
                a[x + 1] = 10000
                count += 1
print(count)
