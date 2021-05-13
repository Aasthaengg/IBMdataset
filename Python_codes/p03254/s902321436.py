n,x = map(int,input().split())
a = sorted(map(int,input().split()))
c=0
for i in a:
    if x<i:
        break
    x-=i
    c+=1
else:
    if x!=0:
        c-=1
print(c)