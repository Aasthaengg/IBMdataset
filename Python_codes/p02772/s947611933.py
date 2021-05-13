n=int(input())
a=list(map(int,input().split()))

x=[]
ans=0
for i in a:
    if i%2==0 :
        x.append(i)
y=[]
for j in x:
    if j%3==0 or j%5==0:
        y.append(j)

if len(x)==len(y):
    print("APPROVED")
else:
    print("DENIED")
