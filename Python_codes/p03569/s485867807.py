s = input()
t = ''
for c in s:
    if c != 'x':
        t += c
if t[::-1] != t:
    print(-1)
    exit()
m = len(t)
l = [0] * (m + 1)
ind = 0
for c in s:
    if c == 'x':
        l[ind] += 1
    else:
        ind += 1
ans = 0
for i in range((m+1)//2):
    ans += abs(l[i] - l[-1-i])
print(ans)