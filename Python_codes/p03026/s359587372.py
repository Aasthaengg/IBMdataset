n=int(input())
e=[[]for i in range(n)]
for i in range(n-1):a,b=map(int,input().split());e[a-1].append(b-1);e[b-1].append(a-1)
c,Q,l,i=sorted(list(map(int,input().split())))[::-1],[0],[0]*n,0
print(sum(c[1:]))
while Q:
 a=Q.pop()
 if l[a]!=0:continue
 l[a]=c[i];i+=1
 for j in e[a]:Q.append(j)
print(*l)