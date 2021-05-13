n=int(input())
a=list(map(int,input().split()))

tmp=0
for item in a:
    tmp=item-tmp
print(tmp)

mount=tmp

for item in a[:-1]:
    mount=(item-mount//2)*2
    print(mount)


    

