K = int(input())

mm = 7
cnt = 1
for i in range(10**7):
    if mm%K==0:
        print(cnt)
        break
    else:
        mm = mm*10+7
        mm %= K
        cnt += 1
else:
    print(-1)