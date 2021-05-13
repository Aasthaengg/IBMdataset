from collections import Counter
s=list(input())
k=int(input())
n=len(s)
s_c=sorted(Counter(s).items())

ans=[]
for i in s_c:
    for j in range(n):
        if s[j]==i[0]:
            ans.append(s[j])
            if j+1<=n-1:
                ans.append("".join([s[j],s[j+1]]))
                if j+2<=n-1 :
                    ans.append("".join([s[j],s[j+1],s[j+2]]))
                    if j+3<=n-1:
                        ans.append("".join([s[j],s[j+1],s[j+2],s[j+3]]))
                        if j+4<=n-1:
                            ans.append("".join([s[j],s[j+1],s[j+2],s[j+3],s[j+4]]))

b=list(set(ans))
b.sort()
print(b[k-1])