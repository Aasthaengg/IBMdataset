x,y,z,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

lis=[]
for i in a:
    for j in b:
        lis.append(i+j)
lis.sort(reverse=True)
ab = lis[:k]

kouho=[]
for sm in ab:
    for tmp in c:
        kouho.append(sm+tmp)

kouho.sort(reverse=True)
kouho = kouho[:k]
for ans in kouho:
    print(ans)