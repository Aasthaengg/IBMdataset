n=input();a=[];b="SHCD"
for i in range(4*13):a.append(b[i/13]+" "+str(i%13+1))
for i in range(n):a.remove(raw_input())
for i in a:print i