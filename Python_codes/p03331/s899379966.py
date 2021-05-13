n = int(input())
a = 0
b = n
ans = 1e9
while (1 < b):
    a += 1
    b -= 1
    sa = str(a)
    sb = str(b)
    sum = 0
    for i in range(len(sa)):
        sum += int(sa[i])
    for i in range(len(sb)):
        sum += int(sb[i])
    ans = min(ans, sum)
print(ans)
