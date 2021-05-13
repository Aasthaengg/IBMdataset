n=int(input())
s=input()
a=set(s)
mod=10**9+7
c=1
for i in a:
    c=c*(s.count(i)+1)%mod
print(c-1)
