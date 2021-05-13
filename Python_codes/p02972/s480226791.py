n=int(input())
a=[0] + list(map(int,input().split()))

boxes=[0]*(n+1)
m=0
b=[]
for i in reversed(range(1,n+1)):
    if sum(boxes[i::i])%2 != a[i]:
        boxes[i]=1
        m+=1
        b.append(i)
print(m)
print(*b)
