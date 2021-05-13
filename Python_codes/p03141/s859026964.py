n = int(input())
l = []
B = 0
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
l.sort(reverse=True,key=lambda x:x[0]+x[1])
ans = 0
for i in range(n):
    if i %2 ==0:
        ans += l[i][0]
    else:
        ans -= l[i][1]
print(ans)