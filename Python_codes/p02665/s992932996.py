n = int(input())
a = list(map(int, input().split()))
l = [[] for i in range(n+1)]
l[-1].append(a[-1])
for i in range(n):
    l[-2-i].append(((l[-1-i][0]+1)//2)+a[-2-i])
    l[-2-i].append((l[-1-i][-1])+a[-2-i])

ans = 1
if l[0][0] == 1:
    num = [1]
    for i in range(n):
        num.append(
            min(
                l[i+1][-1], 
                (num[i]-a[i])*2
                
                )
            )
        ans += num[i+1]

    print(ans)
else:
    print(-1)