s = input()
s2 = []
for i in range(len(s)):
    if s[i] != 'x':
        s2.append(s[i])
if s2 != s2[::-1]:
    print(-1)
    exit()
lis = []
j = 0
cnt = 0
for i in range(len(s)):
    if s[i] == 'x':
        cnt += 1
    else:
        lis.append(cnt)
        cnt = 0

lis.append(cnt)
ans = 0
for i in range(len(lis)//2):
    ans += abs(lis[i]-lis[-(i+1)])
print(ans)
