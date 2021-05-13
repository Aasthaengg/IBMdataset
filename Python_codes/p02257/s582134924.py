import math
N = int(input())
ans = 0

for i in range(N):
    num = int(input())
    if num == 2:
        ans +=1
        continue
    rt = math.ceil(math.sqrt(num))
    div = 2
    bool = True
    while (rt >= div):
        if num % div:
            div += 1
        else:
            bool = False
            break
    if bool:
        ans += 1
print(ans)

