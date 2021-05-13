n = int(input())
a = list(map(int,input().split()))
b = []
c = []
cnt = 1
for i in range(n):
    b.append([a[i]+1,a[i],a[i]-1])
for i in range(n):
    cnt *= len(b[i])
for i in range(n):
    cnt2 = 0
    for j in range(len(b[i])):
        if b[i][j]%2 == 1:
            cnt2 += 1
    c.append(cnt2)
cnt3 = 1
for i in range(n):
    cnt3 *= c[i]
print(cnt-cnt3)
