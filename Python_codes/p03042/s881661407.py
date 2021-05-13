s=input()
ans=[0]*2
a=int(s[:2])
b=int(s[2:])
if 1<=a<=12:
    ans[0]=1
if 1<=b<=12:
    ans[1]=1

if ans[0]==ans[1]==1:
    print('AMBIGUOUS')
elif ans[0]==ans[1]==0:
    print('NA')
elif ans[0]==1 and ans[1]==0:
    print('MMYY')
else:
    print('YYMM')