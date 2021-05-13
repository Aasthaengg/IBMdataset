n=int(input())
a,b=map(int,input().split())
H=list(map(int,input().split()))
d=[]
e=[]
f=[]
for i in range(n):
    k=H[i]
    if k<=a:
        d.append(k)
    elif a<k<=b:
        e.append(k)
    else:
        f.append(k)
print(min(len(d),len(e),len(f)))