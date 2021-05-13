P,Q,R=map(int,input().split())
if P<Q<R or Q<P<R:
    print(P+Q)
if Q<R<P or R<Q<P:
    print(Q+R)
if R<P<Q or P<R<Q:
    print(R+P)
if P==Q==R:
    print(P+Q)
if P==Q<R:
    print(P+Q)
if P==Q>R:
    print(R+P)
if Q==R<P:
    print(Q+R)
if Q==R>P:
    print(P+Q)
if R==P<Q:
    print(R+P)
if R==P>Q:
    print(Q+R)