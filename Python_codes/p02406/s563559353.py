import sys
n=int(input())
a=[]
for i in range(1,n+1):
    if (i%3==0):
        a.append(i)
    else:
        j=str(i)
        for k in range(len(j)):
            if j[k]=="3":
                a.append(i)
                break
for i in a:
    sys.stdout.write(" {0}".format(i))
sys.stdout.write("\n")