n,m = map(int,input().split())
war = [[int(i)-1 for i in input().split()] for _ in range(m)]
war.sort(key=lambda x:x[1])
rm = -1
ans = 0
for i in range(m):
    a,b = war[i]
    if a <= rm: continue
    else:
        ans += 1
        rm = b-1
print(ans)