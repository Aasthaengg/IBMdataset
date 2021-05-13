n = int(input())
t = list(map(int,input().split()))
m = int(input())
l = [list(map(int,input().split())) for i in range(m)]
a,b = [list(i) for i in zip(*l)]
for i in range(m):
    s = list(t)
    j = a[i] - 1
    s[j] = b[i]
    print(sum(s))