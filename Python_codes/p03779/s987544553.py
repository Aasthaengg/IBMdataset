x = int(input())
cnt=0
for i in range(1,10**5):
    cnt += i
    if cnt >= x:
        print(i)
        exit()