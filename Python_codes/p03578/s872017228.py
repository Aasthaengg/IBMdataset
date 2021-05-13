n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
dic={}
for i in range(n):
    if d[i] in dic:
        dic[d[i]]+=1
    else:
        dic[d[i]]=1
for i in range(m):
    if not t[i] in dic:
        print("NO")
        exit()
    if dic[t[i]]==0:
        print("NO")
        exit()
    dic[t[i]]-=1
print("YES")