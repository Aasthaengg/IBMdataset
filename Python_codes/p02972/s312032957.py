n = int(input())
a = list(map(int, input().split()))
box = [0]*n
ans = []
cnt = 0
for i in reversed(range(1, n+1)):
    tmp = 0
    for j in range(i*2, n+1, i):
        tmp ^= box[j-1]
    if a[i-1] != tmp:
        ans.append(i)
        box[i-1] = 1

if (len(ans) == 0):
    print(0)
else:
    print(len(ans))
    print(*ans)
