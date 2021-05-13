N=int(input())
S=[]
cnt=Alist=Blist=0
key=False
for i in range(N):
    s=input()
    cnt+=s.count("AB")
    S=list(s)
    if S[0] == "B":
        Blist+=1
    if S[-1] == "A":
        Alist+=1
    if (S[0] == "B" and S[-1] != "A") or (S[0] != "B" and S[-1] == "A"):
        key = True

cnt += min(Alist,Blist)
if key or min(Alist,Blist)==0:
    print(cnt)
else:
    print(cnt-1)

