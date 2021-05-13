s=list(input())
#　文字の種類ごとにどのタイミングででたか格納
x=[[] for i in range(26)]
n=len(s)
for i in range(n):
    v=ord(s[i])-97
    x[v].append(i)

for i in range(26):
    x[i]=[-1]+x[i]+[n]


ans=float('inf')
for i in range(26):
    cnt=0
    for j in range(1,len(x[i])):
        cnt=max(x[i][j]-x[i][j-1]-1,cnt)
    ans=min(cnt,ans)
print(ans)