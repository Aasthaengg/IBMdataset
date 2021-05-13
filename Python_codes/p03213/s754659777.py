n = int(input())

f = [-1 for i in range(n//2+5)]

for i in range(2,n//2+5):
    if f[i]==-1:
        f[i]=True
        for j in range(i+i,n//2+5,i):
            f[j] = False

f[0]=False
f[1]=False

lis = []
for i in range(n//2+5):
    if f[i]:
        lis.append(i)

div = []

for i in lis:
    num=n
    s=0
    while num>=1:
        num//=i
        s+=num
    div.append(s)

lis2 = [0 for i in range(5)]
for i in div:
    if i>=74:
        lis2[4]+=1
    if i>=24:
        lis2[3]+=1
    if i>=14:
        lis2[2]+=1
    if i>=4:
        lis2[1]+=1
    if i>=2:
        lis2[0]+=1
ans = 0

ans += lis2[1]*(lis2[1]-1)/2*(lis2[0]-2)
ans += lis2[2]*(lis2[1]-1)
ans += lis2[3]*(lis2[0]-1)
ans += lis2[4]

print(int(ans))
