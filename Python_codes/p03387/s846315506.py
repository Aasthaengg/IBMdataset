a = list(map(int,input().split()))
b = []
tmp = max(a)
for i in range(3):
    b.append(tmp-a[i])
if sum(b)%2==0:
    print(sum(b)//2)
else:
    print(sum(b)//2+2)