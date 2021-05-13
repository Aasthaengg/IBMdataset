def calc_t(i,j):
    global t,c
    if i<0 or j<0:
        return n+2
    #print("get t["+str(i)+","+str(j)+"]")
    if t[i][j]==n+1:
        t[i][j]=min(calc_t(i-1,j),calc_t(i,j-c[i])+1)
    return t[i][j]

ri=raw_input().split(" ")
n=int(ri[0])
m=int(ri[1])
ri=raw_input().split(" ")
c=[0]*m
t=[0]*m
for i in range(m):
    c[i]=int(ri[i])
    t[i]=[0]+[n+1]*n if i!=0 else range(n+1)
c=sorted(c)
#print(c)
#print(t)
for a in range(n+1):
    for b in range(m):
        calc_t(b,a)
print(calc_t(m-1,n))