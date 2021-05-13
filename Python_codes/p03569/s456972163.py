s = input()
n = len(s)
s_x = ''.join(s.split('x'))
for i in range(len(s_x)//2):
    if s_x[i] != s_x[-1-i]:
        print(-1)
        exit(0)
ans = 0
i = 0
j = n-1
while i < j:
    if s[i] == 'x' and s[j] == 'x':
        i += 1
        j -= 1
    elif s[i] == 'x':
        ans += 1
        i += 1
    elif s[j] == 'x':
        ans += 1
        j -= 1
    else:
        i += 1
        j -= 1
print(ans)
