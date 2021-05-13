import sys
a=sys.stdin.readline()
res = [int(i) for i in a.split() if i.isdigit()] 
P,Q,R = [res[i] for i in (0,1,2)]
if (P>=1 and P<=100) and (Q>=1 and Q<=100) and (R>=1 and R<=100):
    t1=P+Q
    t2=Q+R
    t3=P+R
    L=[t1,t2,t3]
    L.sort()
    st=L[0]
    print(st)
else:
	print("Error")