n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

ans = []
for i in range(2**n):
    cnt = 0
    for j in range(n):
        if ((i>>j)&1): cnt += a[j]
    ans.append(cnt)
for x in q:
    print('yes' if (x in ans) else 'no')
