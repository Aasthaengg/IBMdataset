S=input()
F=True
T=set()

for s in S:
    F&=(s not in T)
    T.add(s)
    
if F:
    print("yes")
else:
    print("no")
