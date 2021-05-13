A,B,K=map(int,input().split())
if B-A>200:
    k=range(A,A+K)
    l=range(B-K+1,B+1)
    for i in k:
        print(i)
    for i in l:
        print(i)
else:
    s=range(A,B+1)
    t=[x for x in s if A<=x<=A+K-1 or B-K+1<=x<=B]
    t.sort()
    for i in t:
        print(i)
