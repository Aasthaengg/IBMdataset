n=input()
l=list(map(int,input().split()))
a,x=0,0
for i in l:
    if x==i:
        a+=1
        x=0
    else:
        x=i
print(a)