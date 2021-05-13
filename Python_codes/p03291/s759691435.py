s=input()
a_count=[0]
c_count=[0]
q_lcount=[0]
q_rcount=[0]
n=len(s)
for i in range(n):
    if s[i]=='A':
        a_count.append(a_count[i]+1)
        q_lcount.append(q_lcount[i])
    elif s[i]=='?':
        a_count.append(a_count[i])
        q_lcount.append(q_lcount[i]+1)
    else:
        a_count.append(a_count[i])
        q_lcount.append(q_lcount[i])
    if s[n-1-i]=='C':
        c_count.append(c_count[i]+1)
        q_rcount.append(q_rcount[i])
    elif s[n-1-i]=='?':
        c_count.append(c_count[i])
        q_rcount.append(q_rcount[i]+1)
    else:
        c_count.append(c_count[i])
        q_rcount.append(q_rcount[i])
q=q_lcount[n]
ans=0
INF=10**9+7
a=3**q
b=a//3
c=b//3
d=c//3
a=a%INF
b=b%INF
c=c%INF
d=d%INF
for i in range(n):
    if s[i]=='B':
        x=a_count[i]*c_count[n-1-i]*a
        y=a_count[i]*q_rcount[n-1-i]*b
        z=q_lcount[i]*c_count[n-1-i]*b
        w=q_lcount[i]*q_rcount[n-1-i]*c
        ans=(ans+x+y+z+w)%INF
    elif s[i]=='?':
        x=a_count[i]*c_count[n-1-i]*b
        y=a_count[i]*q_rcount[n-1-i]*c
        z=q_lcount[i]*c_count[n-1-i]*c
        w=q_lcount[i]*q_rcount[n-1-i]*d
        ans=(ans+x+y+z+w)%INF
print(int(ans))
