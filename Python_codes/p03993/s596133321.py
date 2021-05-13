N = int(input())
a = list(map(int, input().split()))

count = 0
for index, x in enumerate(a):
    # print (x)
    if index + 1 == a[x - 1]:
        count += 1

print (count // 2)