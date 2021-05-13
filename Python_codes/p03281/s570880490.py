N = int(input())
cnt = 0
for i in range(1,N+1,2):
    ans=0
    for j in range(1,i+1):
        if i % j == 0:
            ans += 1
        else:
            pass
    if ans == 8:
        cnt += 1
    else:
        pass
print(cnt)