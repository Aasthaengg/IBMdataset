h,w=map(int,input().split())
n=int(input())
a=list(map(str,input().split()))

pre=[]
for i in range(n):
    for j in range(int(a[i])):
        pre.append(str(i+1))
for i in range(h):
    if i%2==1:
        sub=pre[w*(i+1)-1:w*i-1:-1]
        pre[w*i:w*(i+1)]=sub
for i in range(h):
    print(' '.join(pre[w*i:w*(i+1)]))