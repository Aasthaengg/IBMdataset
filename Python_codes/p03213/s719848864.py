n = int(input())

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
dic = {}
for num in prime:
    dic[num] = 0
for i in range(1, n + 1):
    j = i
    for num in dic:
        if j == 1:
            break
        while j % num == 0:
            j //= num
            dic[num] += 1
        
        
more_2 = 0
more_4 = 0
more_14 = 0
more_24 = 0
more_74 = 0
for _, j in dic.items():
    if j >= 2:
        more_2 += 1
    if j >= 4:
        more_4 += 1
    if j >= 14:
        more_14 += 1
    if j >= 24:
        more_24 += 1
    if j >= 74:
        more_74 += 1
ans = 0
if more_24 >= 1:
    ans += more_24 * (more_2 - 1)
if more_14 >= 1:
    ans += more_14 * (more_4 - 1)
if more_4 >= 2:
    ans += (more_4 * (more_4 - 1) * (more_2 - 2)) // 2
if more_74 >= 1:
    ans += more_74
print(ans)
