N=int(input())
S=str(input())
m=0
for i in range(N):
    s1=S[i:]
    s2=S[:i]
    m = max(m,len(list(set(s1)&set(s2))))
print(m)