import bisect


N = int(input())
str_l = input()
num = 0
L = []
for v in str_l.split(' '):
    L.append(int(v))

L.sort()
for i in range(N - 1):
    a = L[i]
    for j in range(i, N - 2):
        b = L[j + 1]
        index = bisect.bisect_left(L[j + 2:], a + b)
        num += index
        # for k in range(0, index):
        #     c = (L[j + 2:])[k]
        #     if b + c > a and a + c > b:
        #         num += 1

print(num)