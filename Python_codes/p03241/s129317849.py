n,m=map(int,input().split())
s=set()
for i in range(1,int(m**0.5)+1):
    if m%i==0:
        s.add(i)
        s.add(m//i)
s=sorted(s,reverse=True)
for i in range(len(s)):
    if s[i]<n:
        print(m//s[i-1])
        break
else:print(m)