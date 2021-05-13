n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
a = [[] for i in range(n)]
for i in range(n):
    a[i] = [l[i][0]-l[i][1],l[i][0]+l[i][1]]
a = list(sorted(a,key=lambda x: x[1]))
s,t = [list(i) for i in zip(*a)]
x = t[0]
ans = n
for i in range(1,n):
    if x > s[i]:
        ans -= 1
    else:
        x = t[i]
print(ans)