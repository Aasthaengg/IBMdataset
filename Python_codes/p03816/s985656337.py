import collections

n = int(input())
x = list(map(int, input().split()))

c = collections.Counter(x)
li = []
for i in c.values():
    li.append(i)

li.sort(reverse=True)

for j in range(2):
    for i in range(len(li) - 1):
        if li[i] >= 3 and li[i] % 2 == 0:
            li[i] = 2
        elif li[i] >= 3 and li[i] % 2 != 0:
            li[i] = 1

        if li[i + 1] == 2 and li[i] == 2:
            li[i + 1] = 1
            li[i] = 1
    li.sort(reverse=True)
    if len(li) > 1 and li[0] == 2 and li[1] == 1:
        li[0] -= 1
        li.pop(-1)


print(len(li))


