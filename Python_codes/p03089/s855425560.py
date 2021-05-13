n = int(input())
b = list(map(int, input().split()))

res = []
for i in range(n):
    for j in range(len(b) - 1, -1, -1):
        if b[j] == j + 1:
            res.append(b.pop(j))
            break
    else:
        print('-1')
        exit()

for i in res[::-1]:
    print(i)
