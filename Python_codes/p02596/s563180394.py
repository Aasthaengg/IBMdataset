K = int(input())
dic = {}
x = 0
count = 0
while 1:
    x = (x * 10 + 7) % K
    count += 1
    if x == 0:
        print(count)
        exit()
    if x in dic:
        print(-1)
        exit()
    dic[x] = 1
