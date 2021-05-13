s=input()
t=input()

S=[]
T=[]
for a in s:
    S.append(a)
for a in t:
    T.append(a)
S.sort()
T.sort(reverse=True)


s2=0
t2=0
ans="No"
for i in range(min(len(S),len(T))):
    s2=s2*256+ord(S[i])
    t2=t2*256+ord(T[i])
if s2<t2 :
    ans="Yes"
elif s2==t2 :
    if len(s)<len(t) :
        ans="Yes"
print(ans)