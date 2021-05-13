n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a.sort()
b.sort()
c.sort()

def func(x, y):
    i = 0
    j = 0
    cnt = 0
    s = [0 for i in range(n)]
    while j < n and i < n:
        if y[j] > x[i]:
            cnt += 1
            i += 1
        else:
            s[j] = cnt
            j += 1
    if i == n:
        for k in range(j,n):
            s[k] = cnt
    return s

s1 = func(a, b)
for i in range(1, n):
    s1[i] += s1[i-1]
s2 = func(b, c)
cnt = 0
for i in range(n):
    if s2[i] != 0:
        cnt += s1[s2[i]-1]

print(cnt)