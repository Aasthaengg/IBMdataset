n,m=map(int,input().split())
dic={i:0 for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    dic[a-1]+=1
    dic[b-1]+=1
for i in dic.values():
    print(i)