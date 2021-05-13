n = int(input())

ans = []
for i in range(n//4+1):
    for j in range(n//7+1):
        if 4*i+7*j <= n:
            ans.append(4*i+7*j)
if ans.count(n) != 0:
    print('Yes')
else:
    print('No')