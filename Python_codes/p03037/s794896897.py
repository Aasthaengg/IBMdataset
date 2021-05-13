n,m=map(int, input().split())
l_ans=1
r_ans=n
for i in range(m):
    l,r=map(int, input().split())
    l_ans=max(l_ans,l)
    r_ans=min(r_ans,r)

if r_ans>=l_ans:
    print(r_ans-l_ans+1)
else:
    print(0)