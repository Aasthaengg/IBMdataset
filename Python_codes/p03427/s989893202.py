N=input()
n=int(N)
N3=[int(x) for x in list(N)]
#n=int(N)
if n<10:
    print(n)
    exit()
else:
    ans=sum(N3)
    for i in range(len(N)-1):
        N2=int(N[:i+1])-1
        
        N1=[int(x) for x in list(str(N2))]
        ans=max(ans,sum(N1)+9*(len(N)-i-1))
    print(ans)