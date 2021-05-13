n = int(input())
a = list(map(int, input().split()))
cnt = 0
while True:
    flag = True
    for i in range(n):
        if a[i]%2 == 0:
            a[i] //= 2
        else:
            flag = False
            break
    if not flag:
        break
    cnt += 1
print(cnt)