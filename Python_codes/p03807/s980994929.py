a=int(input())
li = list(map(int,input().split()))

lis = []
for name in li:
    if name % 2 == 1:
        lis.append(name)
        
if len(lis)%2==0:
    print("YES")
else:
    print("NO")