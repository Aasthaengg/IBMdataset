N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

A.sort(key=lambda x: (x[1], x[0]))

gokei = 0
for i in A:
    gokei += i[0]
    if gokei > i[1]:
        print("No")
        break
else:
    print("Yes")