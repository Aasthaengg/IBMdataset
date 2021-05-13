s=int(input())
l=[]
l.append(s)
for i in range(1,1000000):
    if l[i-1]%2==0:
        l.append(int(l[i-1]/2))
    else:
        l.append(3*l[i-1]+1)
    if l[i] in l[0:i]:
        print(i+1)
        break