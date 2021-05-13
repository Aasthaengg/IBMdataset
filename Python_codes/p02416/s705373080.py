a=[]
w=1
while(w!=0):
    w=int(input())
    a.append(w)
a.pop()
for i in a:
    s=0
    for j in range(len(str(i))):
       s+=int(str(i)[j])
    print("{0}".format(s))