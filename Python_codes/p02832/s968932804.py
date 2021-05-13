n = int(input())
a = [1e6] + list(map(int, input().split()))
cnt = 1
exist = False
for i in a:
    if i == cnt:
        exist = True
        cnt += 1
cnt -= 1

if exist:
    print(n - cnt)
else:
    print(-1)