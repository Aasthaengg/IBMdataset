from collections import Counter
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

C_lst = Counter(lst)

cnt = 0
for i in C_lst.values():
    if i % 2 != 0:
        cnt += 1
print(cnt)