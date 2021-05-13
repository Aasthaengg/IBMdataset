n = int(input())
a = list(map(int,input().split()))

flag = 0
ans = 1
cnt = 0
for i in range(n-1):
    if a[i+1] - a[i] > 0 and flag == -1 and cnt > 0:
        flag = 1
        ans += 1
        cnt = 0
    elif a[i+1] - a[i] < 0 and flag == 1 and cnt > 0: 
        flag = -1
        ans += 1
        cnt = 0
    elif a[i+1] - a[i] == 0:
        pass
    elif cnt == 0 and a[i+1] - a[i] > 0:
        flag = 1
        cnt += 1
    elif cnt == 0 and a[i+1] - a[i] < 0:
        flag = -1
        cnt += 1
print(ans)