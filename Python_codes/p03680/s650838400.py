n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))

k = 1
ans = 0
m = 0
while k != 2 and m < n:
    k = lis[k - 1]
    m += 1
if k == 2:
    print(m)
else:
    print("-1")
