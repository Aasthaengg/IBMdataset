s=input()
k=int(input())
lens=len(s)
alp="azyxwvutsrqponmlkjihgfedcb"

ans=[]
for i in range(lens):
    d=alp.index(s[i])
    if k>=d:
        k-=d
        ans.append("a")
    else:
        ans.append(s[i])

las=ans.pop()
alp="abcdefghijklmnopqrstuvwxyz"
ans.append(alp[(alp.index(las)+k)%26])

print("".join(ans))