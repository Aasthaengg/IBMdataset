n=int(input())
l=list(map(int,input().split()))
a1=0
a2=0
s1=0
s2=0
for i,j in enumerate(l):
    s1+=j
    s2+=j
    if i%2:
        if s1>=0:
            a1+=s1+1
            s1=-1
        if s2<=0:
            a2+=-s2+1
            s2=1
    else:
        if s2>=0:
            a2+=s2+1
            s2=-1
        if s1<=0:
            a1+=-s1+1
            s1=1
print(min(a1,a2))