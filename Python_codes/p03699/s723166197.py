N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

li.sort()
if sum(li) % 10 != 0:
    print(sum(li))
else:
    for i in range(N):
        if li[i] % 10 != 0:
            print(sum(li) - li[i])
            exit()

    print(0)
