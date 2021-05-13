n,k,s=map(int,input().split())
a=[]

if (s != 10**9):

    for i in range(k):
        a.append(s)
    for j in range(k,n):
        a.append(s+1)

else:

    for i in range(k):
        a.append(s)
    for j in range(k,n):
        a.append(1)

b=map(str,a)

print(" ".join(b))