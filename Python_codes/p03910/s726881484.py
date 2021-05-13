n = int(input())
sum = 0
skip = -1
for i in range(1,n+1):
    sum += i
    if sum >= n:
        skip = sum - n # 超過分 skip <= n
        last = i
        break
for i in range(1,last+1):
    if i == skip:
        continue
    else:
        print(i)
