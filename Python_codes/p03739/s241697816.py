n = int(input())
lst = [int(x) for x in input().split()]

total = [0, 0]
ret = [0, 0]
for i in range(2):
    for j in range(n):
        total[i] += lst[j]
        if (i + j) % 2 == 0:
            if total[i] >= 0:
                ret[i] += total[i] + 1
                total[i] = -1
        else:
            if total[i] <= 0:
                ret[i] += abs(total[i] - 1)
                total[i] = 1

print(min(ret))