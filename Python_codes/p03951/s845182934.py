n=int(input())
s=input()
r=input()
t=s+r
f=0
for i in range(n):
    if(s[i:]==r[:n-i]):
        t=s[:i]+r
        f=1
        break
if(f==1):
    print(len(t))
else:
    print(2*n)
