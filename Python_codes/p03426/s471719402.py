h,w,d=map(int,input().split())
ind={}
for i in range(h):
    l=list(map(int,input().split()))

    for j in range(w):
        ind[l[j]]=(i,j)
table=[0]*((((h*w)//d).bit_length())*h*w)
now=1
for i in range(1,h*w-d+1):
    a,s=ind[i]
    de,f=ind[i+d]
    table[i-1+d]=abs(a-de)+abs(s-f)
step=2
for i in range(1,((h*w)//d).bit_length()):
    for j in range(1,h*w-step*d+1):
        table[j-1+step*d+i*h*w]=table[j-1+d*step//2+(i-1)*h*w]+table[j-1+d*step+(i-1)*h*w]
    step*=2
#print(*[table[k*h*w:k*w*h+h*w]for k in range(((h*w)//d).bit_length())],sep="\n")
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    times=(r-l)//d
    cost=0
    now=1
    kata=0
    while times:
        if times%2:
            l+=d*now
            cost+=table[l-1+kata*h*w]

        times//=2
        now*=2
        kata+=1
    print(cost)