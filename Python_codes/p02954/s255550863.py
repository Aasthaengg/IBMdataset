s = input()
n = len(s)

a = [0]*n
ans = [0]*n

for i in range(n):
    x = 0
    if s[i] == 'R':
        if i > 0 and a[i-1] > 0:
            x = a[i-1] - 1
        else:
            while s[i+x] == 'R':
                x += 1
    if s[i] == 'L':
        if i > 0 and a[i-1] < 0:
            x = a[i-1] - 1
        else:
            while s[i+x] == 'L':
                x -= 1
    a[i] = x

    if a[i] == 1 or a[i] == -1:
        ans[i] += 1
    elif a[i] % 2 == 0:
        ans[i+ a[i]] += 1
    elif a[i] > 0:
        ans[i+ a[i] - 1] += 1
    elif a[i] < 0:
        ans[i+ a[i] + 1] += 1
        
ans = [str(i) for i in ans]
print(' '.join(ans))