a=[]
w=""
while(w!="0 0"):
    w=input()
    a.append(w)
a.pop()
for st in a:
    s=st.split()
    n=int(s[0])
    x=int(s[1])
    count=0
    for a in range(1,x//3+1):
        for b in range(a+1,(x-a)//2+1):
            if (x-a-b)<=n and b<(x-a-b):
                count+=1
    print("{0}".format(count))