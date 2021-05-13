ans=[]
N=int(input())
def saiki(A):
    eigo="abcdefghijklmnopqrstuvwxyz"
    if len(A)==N:
        B="".join(A)
        ans.append(B)
        return
    for i in range(len(set(A))+1):
        A.append(eigo[i%26])
        saiki(A)
        A.pop()
saiki([])
ans.sort()
for i in ans:
    print(*i,sep="")