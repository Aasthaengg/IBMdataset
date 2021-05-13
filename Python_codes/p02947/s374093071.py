from collections import Counter
n=int(input())
ans=[]
tt=0
for i in range(n):
    s=list(input())
    s.sort()
    s="".join(s)
    ans.append(s)
l=Counter(ans)
c=l.most_common()
for i,j in c:
    tt+=j*(j-1)//2
print(tt)