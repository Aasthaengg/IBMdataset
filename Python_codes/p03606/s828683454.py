N = int(input())
ans = 0
l=[]
r=[]
for i in range(N):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)

for i in range(N):
    ans += (abs(r[i]-l[i])+1)

if ans<=10**5:
    print(ans)
else:
    print(10**5)