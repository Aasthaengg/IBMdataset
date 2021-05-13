N, M = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(N)])

count = 0
money = 0
for list in arr:
    for i in range(list[1]):
        money += list[0]
        count += 1
        if count == M:
            print(money)
            exit()



