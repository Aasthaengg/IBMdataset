N = int(input())
a = list(map(int, input().split()))

ans = 0
num = -1
for i in range(N):
    cnt = 0
    if(i <= num):
        continue
    for j in range(i+1, N):
        if(a[i] == a[j]):
            cnt += 1
            num = j
        else:
            break
    if(cnt%2 == 0):
        ans += cnt//2
    else:
        ans += cnt//2+1
print(ans)