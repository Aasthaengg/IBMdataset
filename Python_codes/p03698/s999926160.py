s = input()

visited = [False] * 26
flg = True
for i in range(len(s)):
    x = ord(s[i]) - 97
    if visited[x]:
        flg = False
        break
    visited[x] = True
print('yes') if flg else print('no')