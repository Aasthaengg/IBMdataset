n,k=map(int,input().split())
seq=input()

if seq[n-1]=="0":
    seq=seq+"1"
else:
    seq=seq+"0"

l=[]

if seq[0]=="0":
    l.append(0)

st=0
for i in range(n):
    if seq[i:i+2] in ("01","10"):
        l.append(i+1-st)
        st=i+1

if len(l)%2==0:
    l.append(0)

if 2*k+1>=len(l):
    print(sum(l))
else:
    lis=[sum(l[0:2*k+1])]
    for i in range((len(l)-2*k-1)//2):
        lis.append(lis[i]-l[2*i]-l[2*i+1]+l[2*i+2*k+1]+l[2*i+2*k+2])
    print(max(lis))