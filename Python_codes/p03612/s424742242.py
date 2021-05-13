N = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(len(p)):
    if i + 1 == p[i]:
        if i + 1 != len(p):
            tmp = p[i]
            p[i] = p[i + 1]
            p[i + 1] = tmp
            count += 1
        else:
            tmp = p[i]
            p[i] = p[i - 1]
            p[i - 1] = tmp
            count += 1

print(count)
