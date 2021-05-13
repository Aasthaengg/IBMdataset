n = int(input())
a = list(map(int, input().split()))

rate = [i*400-1 for i in range(1,9)]
over = 0
d = {}

for i in range(n):
    if a[i] > rate[-1]:
        over += 1
    else:
        for j in range(len(rate)):
            if a[i] <= rate[j]:
                if rate[j] not in d:
                    d[rate[j]] = 1
                else:
                    d[rate[j]] = d[rate[j]] + 1
                break


print(max(len(d), 1), len(d)+over)


