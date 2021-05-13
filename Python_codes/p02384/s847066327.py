sokumen={1:[2,3,5,4,2],2:[6,3,1,4,6],3:[2,6,5,1,2],4:[2,1,5,6,2],5:[1,3,6,4,1],6:[5,3,2,4,5]}
number=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    u,f=map(int,input().split())
    u=number.index(u)+1
    f=number.index(f)+1
    ans=sokumen[u][sokumen[u].index(f)+1]
    print(number[ans-1])
