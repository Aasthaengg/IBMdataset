n = int(input())
a = list(map(int,input().split()))

if n <= 2:
    print(1)
    exit()

f = 0
cnt = 0
if a[0] < a[1]:
    f = 1
elif a[0] > a[1]:
    f = 2
tmp = a[1]

for i in range(2,n):
    if tmp < a[i]:
        if f == 2:
            cnt += 1
            f = 0
        elif f == 0:
            f = 1
    elif tmp > a[i]:
        if f == 1:
            cnt += 1
            f = 0
        elif f == 0:
            f = 2
    tmp = a[i]
cnt += 1

print(cnt)