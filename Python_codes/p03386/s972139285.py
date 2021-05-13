a,b,k=map(int,input().split())

lst=[]
for i in range(a,a+k):
    if i<=b:
        lst.append(i)

for i in range(b-k+1,b+1):
    if a<=i and not i in lst:
        lst.append(i)

print(*lst)