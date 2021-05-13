from collections import Counter

N=int(input())
A=list(map(int,input().split()))
p=10**9+7

A_=Counter(A)
A_=A_.most_common()

flag=N%2

for a in A_:
    if a[0]%2==flag:
        print(0)
        exit()
    elif a[0]==0 and a[1]!=1:
        print(0)
        exit()
    elif a[0]!=0 and a[1]!=2:
        print(0)
        exit()

ans=1
for i in range(N//2):
    ans*=2
    ans%=p
print(ans%p)