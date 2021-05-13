n=int(input())
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append([x,y])
l=sorted(l)
s=set()
for j in range(n-1):
    for k in range(j,n):
        s.add((l[k][0]-l[j][0],l[k][1]-l[j][1]))
s_l=sorted(list(s))
cnt=[0]*len(s_l)
dic={}
for i in range(len(s_l)):
    dic[s_l[i]]=i
for j in range(n-1):
    for k in range(j+1,n):
        cnt[dic[(l[k][0]-l[j][0],l[k][1]-l[j][1])]]+=1
if n==1:
    print(1)
    exit()
print(n-max(cnt))
