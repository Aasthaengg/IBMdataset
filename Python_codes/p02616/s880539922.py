n,k = map(int, input().split())
a = list(map(int, input().split()))

mod=10**9+7
a.sort()

if n==k:
    ans=1
    for num in a:
        ans*=num
        ans%=mod
    print(ans)
    exit()

if a[-1]<0: # all a is minus
    if k%2==1: # ans is minus
        a.sort(reverse=True)
        ans=1
        for num in a[:k]:
            ans*=num
            ans%=mod
        print(ans)
        exit()

# ans>=0

ans=1
if k%2==1:
    ans=a[-1]
    a.pop(-1)
    k-=1

pz_a=[]
m_a=[]

for num in a:
    if num<0:
        m_a.append(num)
    else:
        pz_a.append(num)
pz_a.sort(reverse=True)

c2_a=[]
lastnum=-1
for i in range(len(pz_a)):
    num1=pz_a[i]
    if lastnum==-1:
        lastnum=num1
    else:
        c2_a.append(lastnum*num1)
        lastnum=-1

lastnum=1
for i in range(len(m_a)):
    num1=m_a[i]
    if lastnum==1:
        lastnum=num1
    else:
        c2_a.append(lastnum*num1)
        lastnum=1

c2_a.sort(reverse=True)

for num in c2_a[:k//2]:
    ans*=num
    ans%=mod

print(ans)
