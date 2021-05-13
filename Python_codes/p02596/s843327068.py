K = int(input())
a = 7 % K
cnt = 1
while a:
    a = (10*a+7) % K
    cnt += 1
    if K < cnt:
        cnt = -1
        break
print(cnt)