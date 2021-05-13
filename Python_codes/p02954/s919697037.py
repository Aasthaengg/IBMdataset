s = input()
ans = [0] * len(s)
for i in range(2):
    cnt = 0
    for j in range(len(s)):
        if s[j] == 'R':
            cnt += 1
        else:
            ans[j-1] += (cnt+1)//2
            ans[j] += cnt//2
            cnt = 0

    ans = ans[::-1]
    s = s[::-1]
    s = s.replace('R', 'X').replace('L', 'R').replace('X', 'L')

for i in range(len(s)):
    print(ans[i], end=' ')
print()
