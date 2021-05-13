n = int(input())
list = []
ans = 0
for i in range(n):
    x,u=input().split()
    list.append((float(x), u))
    if list[i][1]=='JPY':
        ans += list[i][0]
    else:
        ans += list[i][0] * 380000
print(ans)