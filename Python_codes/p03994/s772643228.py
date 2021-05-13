s=input()
K=int(input())
ns=len(s)
ls=list(s)
for i in range(ns):
    if K==0:
        break
    if ls[i]=="a":
        continue
    toa=ord("z")+1-ord(ls[i])
    #print("toa",toa)
    if toa<=K:
        ls[i]="a"
        #K-=(ord("z")+1-ord(s[i]))
        K-=toa
        #print("K",K)
ls[-1]=chr(ord(ls[-1])+K%26)
#ans=str(ls)
ans="".join(ls)
print(ans)
