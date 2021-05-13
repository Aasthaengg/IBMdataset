n = int(input())
s = [input().split() for _ in range(n)]
s.reverse()
x = input()
ans = 0
for i in range(n):
    if s[i][0] == x:
        print(ans)
        exit()
    else:
        ans += int(s[i][1])