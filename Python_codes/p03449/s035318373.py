n = int(input())
l = []
for _ in range(2):
    a = list(map(int,input().split()))
    l.append(a)

if n == 1:
    print(l[0][0]+l[1][0])
    exit()

m1 = []
m2 = []
m1.append(0)
m1.append(l[0][0])
m2.append(0)
m2.append(l[1][0])

for i in range(1,n):
    m1.append(m1[i]+l[0][i])
    m2.append(m2[i]+l[1][i])

ans = [0]*n
for j in range(1,n+1):
    ans[j-1] = m1[j]+(m2[n]-m2[j-1])


print(max(ans))