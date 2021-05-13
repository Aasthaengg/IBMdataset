n = int(input())
s = [0] * 5
for i in range(n):
    l = input()
    l = l[0]
    if l == 'M':
        s[0] += 1
    elif l == 'A':
        s[1] += 1
    elif l == 'R':
        s[2] += 1
    elif l == 'C':
        s[3] += 1
    elif l == 'H':
        s[4] += 1
    else:
        pass
ans = 0
a = [[0,1,2],[0,1,3],[0,1,4],[0,2,3],[0,2,4],[0,3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
for i in range(10):
    ans += s[a[i][0]] * s[a[i][1]] * s[a[i][2]]
print(ans)