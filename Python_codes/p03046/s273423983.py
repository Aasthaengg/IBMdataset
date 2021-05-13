M,K=map(int,input().split())

if 2**M-1<K:
    print(-1)
    exit()
if M==1:
    if K==0:
        print(0,0,1,1)
    if K==1:
        print(-1)
    exit()

res=0
li=[]
for i in range(2**M):
    if i==K:
        continue
    li.append(i)
ans=[K]+li+[K]+li[::-1]
print(*ans)