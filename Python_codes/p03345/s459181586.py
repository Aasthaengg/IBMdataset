A,B,C,K=map(int,input().split())
l=[A,B,C]
#l.sort(reverse=True)
if K%2==0:
    if abs(A-B)>10**18:
        print("Unfair")
    else:
        print(A-B)
else:
    if abs(B-A)>10**18:
        print("Unfair")
    else:
        print(B-A)

