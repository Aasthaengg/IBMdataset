n = int(input())
b = list(map(int, input().split()))

lst = []
for i in range(n, 0, -1):
    for j in range(i - 1, -1, -1):
        if b[j] == j + 1:
            lst.append(j + 1)
            b.pop(j)
            break
    else:
        print(-1)
        exit()

for num in lst[::-1]:
    print(num)