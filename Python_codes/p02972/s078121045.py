import math

N = int(input())
a = list(map(int,input().split()))
b = []
x = math.ceil(N/2)
check = 0

for i in reversed(range(N-x)):
    flag = a[i]
    mul = i + 1
    for j in range(mul + mul -1,N,mul):
        check += a[j]
    if (check % 2 == 0 and flag == 0) or (check % 2 == 1 and flag == 1):
        a[i] = 0
    else:
        a[i] = 1
    check = 0

ans = a.count(1)
print(ans)
if ans == 0:
    exit()

for i in range(N):
    if a[i] == 1:
        b.append(i+1)

print(*b)