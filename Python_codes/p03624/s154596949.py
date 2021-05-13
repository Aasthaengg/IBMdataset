a=list(input())
n=[]
for i in range(97, 123):
    n.append(chr(i))
a=list(set(a))
ans=[]
for i in n:
    if i not in a:
        ans.append(i)
if ans==[]:
    print('None')
else:
    print(ans[0])