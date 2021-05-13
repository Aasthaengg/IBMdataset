n = int(input())
l = []
for i in range(1,n+1):
    s,p = input().split()
    t = [s,int(p),i]
    l.append(t)
l.sort()
def check(m,i):
    z = list(l[m:i])
    z.sort(key = lambda x: x[1] , reverse = True)
    for j in range(i-m):
        print(z[j][2])
m = 0
for i in range(1,n):
    if l[m][0] != l[i][0]:
        check(m,i)
        m = i
check(m,n)