def gusuuhantei(i):
    count = 0
    num = i
    while True:
        if num % 2 ==0 and not num == 0:
            num = num / 2
            count += 1
        else:
            break
    return count
N = int(input())
li = [-1]*(N+1)
for i in range(1, N+1):
    li[i] = gusuuhantei(i)
Maxcount = max(li)
index = li.index(Maxcount)
print(index)