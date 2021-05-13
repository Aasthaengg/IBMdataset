N = int(input())
works = []
time = 0
for _ in range(N):
    cost, deadline = map(int, input().split())
    works.append((deadline, cost))

works.sort()
# print(works)

for item in works:
    deadline, cost = item[0], item[1]
    # print(deadline)
    # print(cost)
    time += cost
    if time > deadline:
        print('No')
        exit()

print('Yes')
