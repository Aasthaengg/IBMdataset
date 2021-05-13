N=int(input())
que=[]
for i in range(N):
    s,p=list(input().split())
    que.append((s,int(p),i+1))
que.sort(key=lambda x:(x[0],-x[1]))
for x in que:
    print(x[-1])