from collections import Counter
n=int(input())
s=[]
for _ in range(n):
    temp=sorted(list(input()))
    s.append("".join(temp))
s_count=Counter(s)
ans=0
for i in s_count:
    ans+=((s_count[i])*(s_count[i]-1))//2
print(ans)