n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(n - 1):
    b.append(b[-1] + a[i + 1])
f = [True, False]
ans = float("inf")
for i in f:
    flag = i
    count = 0
    num = 0
    for j in range(n):
        if flag == True:
            if b[j] + num <= 0:
                count += 1 - b[j] - num
                num += 1 - b[j] - num
            flag = False
        else:
            if b[j] + num >= 0:
                count += b[j] + num + 1
                num -= b[j] + num + 1
            flag = True
    ans = min(ans, count)
print(ans)