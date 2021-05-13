n=int(input())
S=input()
a=S.count("E")
m=a
for s in S:
    if s=="E":
        a-=1
    m=min(m,a)
    if s=="W":
        a+=1
print(m)