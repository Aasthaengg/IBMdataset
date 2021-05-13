S=int(input())
leng=len(str(S))

bin(2**leng-1)
ans=0
if leng==1:
    print(S)
    exit()
for i in range(2**(leng-1)):
    bid=bin(2**(leng-1)+i)
    start=0
    for j in range(3,len(str(bid))):
        if bid[j]=='1':
            ans+=int(str(S)[start:j-2])
            start=j-2
        if j==len(str(bid))-1:
            ans+=int(str(S)[start:j-1])
print(ans)