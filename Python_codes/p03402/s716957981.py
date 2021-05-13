a,b=map(int,input().split())
a-=1
b-=1
s=[".","#"]*50
t=["#"]*100
q=["#","."]*50
p=["."]*100
ans=[]
#白について
aaa=a//50
aa=a%50
for i in range(aaa):
    ans.append(s)
    ans.append(t)
x=[".","#"]*aa+["#","#"]*(50-aa)
ans.append(x)
ans.append(t)
ans.append(p)

bbb=b//50
bb=b%50
for i in range(bbb):
    ans.append(q)
    ans.append(p)
x=["#","."]*bb+[".","."]*(50-bb)
ans.append(x)

print(len(ans),100)
for u in ans:
    print("".join(u))