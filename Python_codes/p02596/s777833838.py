k = int(input())
num = 0
if not k%2:
    print(-1)
else:
    for i in range(k):
        num = (num*10+7)%k
        if num == 0:
            print(i+1)
            break
    else:
        print(-1)