n = int(input())
data = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i):
        if i == j:
            continue
        else:
            sum +=  data[i] * data[j]
            # print(sum)

print(sum)
