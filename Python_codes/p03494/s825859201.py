n = int(input())
a = list(map(int, input().split()))

i = 0
per = True
while per == True:
    for index in range(n):
        num = a[index]
        ans = divmod(num, 2)
        if num == 0 or ans[1] != 0:
            per = False
            break
        a[index] = ans[0]
    if per == True:
        i += 1
print(i)