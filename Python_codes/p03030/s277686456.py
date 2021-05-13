n=int(input())
ans=[]
for i in range(n):
    s,p=input().split()
    ans.append([s,int(p),i+1])

anspoint=sorted(ans,key=lambda x:x[1], reverse=True)
anscity=sorted(anspoint,key=lambda x:x[0])

for i in anscity:
    print(i[2])