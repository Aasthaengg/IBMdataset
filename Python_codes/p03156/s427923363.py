A=input()
A,B=input().split()
A=int(A)
B=int(B)
P=input().split()
c=[0]*3
for i in P:
        i=int (i)
        if i <= A:
                c[0]+=1
        elif i <= B:
                c[1]+=1
        else :
                c[2]+=1
c.sort()
print(c[0])