n = int(input())
a = []
for _ in range(5):
    a.append(int(input()))
min_num = a[0]
for i in range(5):
    if min_num > a[i]:
        min_num = a[i]
res = n // min_num + 5
if n % min_num == 0:
    res -= 1
print(res)
