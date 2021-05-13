s=input()
import collections
p=collections.Counter(s)
#print(p[max(p)])
if len(p)==3:
    if p[max(p,key=p.get)]-p[min(p,key=p.get)]<2:
        print("YES")
    else:
        print("NO")
if len(p)==2:
    if p[max(p,key=p.get)]>1:
        print("NO")
    else:
        print("YES")
if len(p)==1:
    if p[max(p,key=p.get)]==1:
        print("YES")
    else:
        print("NO")