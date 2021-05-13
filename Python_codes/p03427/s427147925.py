n=input()
nn=len(n)
if nn==1:
    print(n)
    exit()
flg=True
for i in range(1,nn):
    if n[i]!="9":
        flg=False
ans=0
if flg:
    for i in range(nn):
        ans+=int(n[i])
    print(ans)
    exit()
if flg==False:
    if n[0]!="1":
        print(int(n[0])-1+9*(nn-1))
    if n[0]=="1":
        print(9*(nn-1))