x = int(input())
cnt = 0
for i in range(1,x+1):
    cnt += i
    if cnt >= x:
        print(i)
        break
