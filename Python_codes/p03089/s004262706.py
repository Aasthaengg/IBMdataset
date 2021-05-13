n = int(input())
b = list(map(int, input().split()))
i = n - 1
ans = []
while i > -1 and n != 0:
    if b[i] == i + 1:
        ans.append(b.pop(i))
        n -= 1
        i = n - 1
    else:
        i -= 1
if n == 0:
    ans.reverse()
    print(*ans, sep='\n')
else:
    print(-1)