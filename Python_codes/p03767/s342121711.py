n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)
list = []

for i, j in enumerate(a):
    if i % 2 == 1:
        list.append(j)

answer = sum(list[0 : n])

print(answer)