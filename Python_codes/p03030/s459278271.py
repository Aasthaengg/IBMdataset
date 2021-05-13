n = int(input())
info = {}
for i in range(1, n + 1):
    s, p = input().split()
    info[i] = (s, int(p))

ans = list(info.keys())
ans.sort(key=lambda i: info[i][1], reverse=True)
ans.sort(key=lambda i: info[i][0])
for i in ans:
    print(i)
