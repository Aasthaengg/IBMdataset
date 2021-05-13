alp='abcdefghijklmnopqrstuvwxyz'
S=input()
a=[0 for i in range(26)]
for s in S:
    a[alp.index(s)]+=1
if a.count(0)>=1:
    print(alp[a.index(0)])
else:
    print("None")