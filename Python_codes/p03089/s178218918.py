N=int(input())
B=list(map(int,input().split()))
n=1
ans=[]
l=len(B)
while B:
    l=len(B)
    for i in range(len(B)):
        if B[::-1][i]==l:
            ans.append(l)
            del B[len(B)-1-i]
            break
        else:
            l-=1
    else:
        print(-1)
        exit()
print(*reversed(ans),sep="\n")