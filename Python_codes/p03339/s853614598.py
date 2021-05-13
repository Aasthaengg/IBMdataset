n=int(input())
s=input()
w=s.count("W")
e=s.count("E")
t=0
ans=n
for i in range(n):
    if s[i]=="E":
        e-=1
    tmp=e+t
    if tmp<ans:
        ans=tmp
    if s[i]=="W":
        t+=1
print(ans)