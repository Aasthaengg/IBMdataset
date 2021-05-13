h, w, n = map(int, input().split())

dic = {}

for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if a + i <= 0 or a + i >= h - 1 or b + j <= 0 or b + j >= w - 1:
                continue
            if (a+i, b+j) in dic:
                dic[(a+i, b+j)] += 1
            else:
                dic[(a+i, b+j)] = 1

count = [0]*10
for i in dic.values():
    count[i] += 1
count[0] = (h-2)*(w-2)-sum(count)
for i in range(10):
    print(count[i])
