n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
tasks.sort(key = lambda x:(x[1],-x[0]))
acc = 0
for i in tasks:
    acc += i[0]
    if acc > i[1]:
        print('No')
        exit()
print('Yes')