x = int(input())

cnt = 0
for i in range(10**5):
    cnt += i
    if x <= cnt:
        print(i)
        break
