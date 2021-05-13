n = int(input())
a = list(map(int, input().split()))
lis = [0] * (max(a) + 1)
for i in a:
    lis[i] += 1
cnt = 0
for i in lis:
    cnt += max(0,i-1)
ans = len(set(a))
if cnt % 2 == 0:
    print(ans)
else:
    print(ans - 1)