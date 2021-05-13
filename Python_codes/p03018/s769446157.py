s = list(input())
li = []
n = len(s)
ans = 0
b = False
for i in range(n-1):
    if b:
        b = False
        continue
    if s[i] + s[i+1] == 'BC':
        li.append('D')
        b = True
    if s[i] == 'B' and s[i+1] != 'C':
        li.append('E')
    if s[i] == 'C':
        li.append('E')
    if s[i] == 'A':
        li.append('A')
cnt = 0
for i in range(len(li)):
    if li[i] == 'A':
        cnt += 1
    elif li[i] == 'E':
        cnt = 0
    else:
        ans += cnt
print(ans)