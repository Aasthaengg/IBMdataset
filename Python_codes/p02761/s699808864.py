n, m = map(int, input().split())
ans = [0] * n

for i in range(m):
    s, c = map(int, input().split())

    if(ans[s-1] != 0 and ans[s-1] != c):
        print(-1)
        exit()
    elif(n != 1 and s == 1 and c == 0):
        print(-1)
        exit()
    else:
        ans[s-1] = c

if(ans[0] == 0 and len(ans) > 1):
    print(str(1) + "" .join(map(str, ans[1:])))
else:
    print("".join(map(str, ans)))
