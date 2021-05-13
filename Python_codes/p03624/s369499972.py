S=input()

U=set([chr(ord("a")+k) for k in range(26)])
T=set()
for s in S:
    T.add(s)

V=list(U-T)
V.sort()

if V:
    print(V[0])
else:
    print("None")
