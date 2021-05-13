N = int(input())
alist=[]
if N ==1:
    print("Yes")
    print("2")
    print("1 1")
    print("1 1")
    exit()
if N==2:
    print("No")
    #print("2")
    #print("2 1 2")
    #print("2 1 2")
    exit()

for i in range(2000):
    if i*(i+1)/2 > 100000:
        break
    else:
        alist.append(int(i*(i+1)/2) )

#print(alist)

if N in alist:
    print("Yes")
else:
    print("No")
    exit()

tate=alist.index(N)+1
yoko=alist.index(N)
#print(tate,yoko)
s=[]
tmp=[]
cnt=1
for j in range(tate):
    stmp=[]
    ntmp=[]
    for l in range(len(tmp)):
        #print("nowtmp:",tmp)
        stmp.append(tmp[l].pop(0))
        #print("tmp:",stmp)
    for m in range(yoko-len(stmp)):
        stmp.append(cnt)
        ntmp.append(cnt)
        #print("cnt:",stmp)
        cnt=cnt+1
    #print(stmp)
    s.append(stmp)
    #print("append ntmp:",ntmp)
    tmp.append(ntmp)
    tmp2=[x for x in tmp if x ]
    tmp=tmp2

print(len(s))

for j in range(len(s)):
    #print(" ".join( s[j] ))
    #list1= [ str(s[j][i]) for i in range(len(s[j]))]
    print(len(s[j])," ".join(str(i) for i in s[j]))
