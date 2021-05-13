n,m = map(int,input().split())

ok = True
num = [-1]*n
for i in range(m):
    s,c = map(int,input().split())
    s -= 1
    if n >= 2 and s == 0 and c == 0:
        ok = False
        break
    elif num[s] == -1:
        num[s] = c
    elif num[s] != c:
        ok = False
        break
if ok == False:
    print(-1)
    exit()
for i in range(n):
    if n >= 2 and i == 0:
        if num[i] == -1:
            num[i] = 1
    else:
        if num[i] == -1:
            num[i] = 0
ans = [str(num[i]) for i in range(n)]
print("".join(ans))