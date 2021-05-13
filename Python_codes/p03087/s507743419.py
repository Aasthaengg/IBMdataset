n,q=map(int,input().split())
s=input()
ans_l=[0]*n
for i in range(n-1):
    tmp=s[i]+s[i+1]
    if tmp=='AC':
        ans_l[i+1]=ans_l[i]+1
    else:
        ans_l[i+1]=ans_l[i]
for i in range(q):
    l,r=map(int,input().split())
    print(ans_l[r-1]-ans_l[l-1])