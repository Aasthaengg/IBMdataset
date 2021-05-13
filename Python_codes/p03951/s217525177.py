n=int(input())
s=input()
t=input()

n_s=len(s)
n_t=len(t)
l=[]
for i in range(n_s):
    for j in range(n_t):
        l.append(s[:i]+t[j:])
ans=s+t
for c in l:
    if c[:n_s]==s and c[len(c)-n_t:]==t:
        if len(ans)>len(c):
            ans=c

print(len(ans))