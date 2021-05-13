n = int(input())
a = [0]
a.extend(list(map(int,input().split())))
a.append(0)

s = []
for i in range(n+1):
    s.append(abs(a[i]-a[i+1]))
ss = sum(s)
for i in range(1,n+1):
    print(ss+abs(a[i-1]-a[i+1])-(abs(a[i-1]-a[i])+abs(a[i]-a[i+1])))
