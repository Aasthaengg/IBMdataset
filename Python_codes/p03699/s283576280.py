N = int(input())

S=[]
for n in range(N):
    S.append(int(input()))

S.sort(reverse=True)

S_cumsum = []
S_not_10 = 10**10
s_=0
for s in S:
    if s % 10 !=0 and S_not_10 > s:
        S_not_10 = s
    s_+=s
    S_cumsum.append(s_)
    
ans=0
if s_ % 10 !=0:
    ans=s_
    
elif S_not_10 != 10**10:
    ans = s_-S_not_10
else:
    ans=0
print(ans)