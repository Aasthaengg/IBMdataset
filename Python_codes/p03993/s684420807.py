n=int(input())
a=list(map(int,input().split()))
c=0
for i,b in enumerate(a):
    if i+1==a[b-1]:c+=1
print(c//2)