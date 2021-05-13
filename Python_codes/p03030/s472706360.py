n = int(input())
spi = sorted([list(input().split())+[i+1] for i in range(n)])
ans = []
before = ""
for s,p,i in spi:
    if ans == []:
        ans = [[int(p),i]]
        before = s
    else:
        if before == s:
            ans.append([int(p),i])
        else:
            for j in sorted(ans)[::-1]: print(j[1])
            ans = [[int(p),i]]
            before = s
if ans:
    for i in sorted(ans)[::-1]: print(i[1])