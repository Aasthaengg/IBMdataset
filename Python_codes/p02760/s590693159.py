import itertools
a=[list(map(int,input().split())) for i in range(3)]
a=list(itertools.chain.from_iterable(a))
n=int(input())
b=[]

for i in range(n):
  b.append(int(input()))

ans=['-']*9

for i in a:
  if i in b:
    ans[a.index(i)]='+'

if ans[0]==ans[1]==ans[2]=='+' or ans[3]==ans[4]==ans[5]=='+' or ans[6]==ans[7]==ans[8]=='+'\
   or ans[0]==ans[3]==ans[6]=='+' or ans[1]==ans[4]==ans[7]=='+' or ans[2]==ans[5]==ans[8]=='+'\
   or ans[0]==ans[4]==ans[8]=='+' or ans[2]==ans[4]==ans[6]=='+':
  print('Yes')
else:
  print('No')