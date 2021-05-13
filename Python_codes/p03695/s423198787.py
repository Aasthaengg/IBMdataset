N=int(input())
*A,=map(int,input().split())

count=[min(i//400,8)for i in A]
c8=count.count(8)

if c8>0:
    print(max(len(set(count))-1,1),len(set(count))+c8-1)
else:
    print(len(set(count)),len(set(count)))