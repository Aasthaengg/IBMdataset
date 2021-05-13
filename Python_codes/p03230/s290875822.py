import math

n = int(input())
num = 2 * n
tmp = int(math.sqrt(num))
if tmp * (tmp + 1) != num:
    print("No")
    exit()
print("Yes")
print(tmp + 1)
lst = [[] for _ in range(tmp + 1)]
last = 1
for i in range(tmp + 1):
    print(tmp, end = " ")
    cnt = 0
    for j in range(i):
        x = lst[j].pop()
        print(x, end = " ")
        cnt += 1
    for k in range(cnt, tmp):
        print(last, end = " ")
        lst[i].append(last)
        last += 1
        
    print()