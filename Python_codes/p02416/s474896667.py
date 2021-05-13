#coding: UTF-8

while True:
    buf = list(input())
    if len(buf) == 1 and int(buf[0]) == 0:
        break
    else:
        ans = 0
        for i in range(len(buf)):
            ans += int(buf[i])
        print(ans)
