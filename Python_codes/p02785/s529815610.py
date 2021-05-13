n,k=map(int,input().split())
H=list(map(int,input().split()))
H.sort()
if k!=0:
    print(sum(H[:-k]))
else:
    print(sum(H))