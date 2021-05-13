n = int(input())
b = list(map(int, input().split()))

ans = []
flg = True
for x in range(n):
    memo = -1
    for i in range(len(b)):
        if b[i] == i+1:
            memo = i
    if memo == -1:
        flg = False
        break
    ans.append(memo+1)
    b.pop(memo)

if flg:
    print(*ans[::-1], sep='\n')
else:
    print(-1)
