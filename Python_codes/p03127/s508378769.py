n=int(input())
a=sorted(set([int(x) for x in input().split()]))

while len(a)!=1:
    if a[0]==0:
        a=a[1:]
    for i in range(1,len(a)):
        a[i]%=a[0]
    a=sorted(set(a))

print(a[0])
