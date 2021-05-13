n,m = map(int,input().split())
ans = []
for i in range(n):
    ans.append('m')
err = 0
for i in range(m):
    s,c = map(int,input().split())
    if ans[s-1] == 'm':
        ans[s-1] = str(c)
    else:
        if ans[s-1] != str(c):
            err = 1
if n == 1:
    if ans[0] == 'm':
        ans[0] = '0'
else:
    if ans[0] == '0':
        err = 1
    else:
        if ans[0] == 'm':
            ans[0] = '1'
for i in range(1,n):
    if ans[i] == 'm':
        ans[i] = '0'
#print(ans)
if err == 0:
    if n == 1:
        print(ans[0])
    elif n == 2:
        print(ans[0]+ans[1])
    else:
        print(ans[0]+ans[1]+ans[2])
else:
    print(-1)