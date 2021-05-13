s=input()
x,y=map(int,input().split())

l=[0]
for i in s:
    if i=="F":
        l[-1]+=1
    else:
        l.append(0)
lx=[0]
ly=[0]
for i in range(len(l)):
    if i==0:
        continue
    if i%2==0:
        lx.append(l[i])
    else:
        ly.append(l[i])

q=[l[0]]
for i in lx:
    ll=set()
    for j in q:
        ll.add(j+i)
        ll.add(j-i)
    q=list(ll)
if x not in set(q):
    print("No")
    exit()

q=[0]
for i in ly:
    ll=set()
    for j in q:
        ll.add(j+i)
        ll.add(j-i)
    q=list(ll)
if y in set(q):
    print("Yes")
else:
    print("No")