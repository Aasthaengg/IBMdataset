n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist=list(map(int,input().split()))

sum=0
bef=-2

for a in alist:
    sum += blist[a-1]
    if bef + 1 == a:
        sum += clist[bef-1]
    bef = a

print(sum)