n=int(raw_input())
a=map(int,raw_input().split())
q=int(raw_input())
m=map(int,raw_input().split())
ans=set()
p=(1<<n)-1
while p:
    w=str(bin(p))[2:]
    bits='0'*(n-len(w))+w
    p-=1
    k=0
    for i,j in enumerate(bits):
        if j=='1':
            k+=a[i]
    ans.add(k)
for i in m:
    print 'yes' if i in ans else 'no'