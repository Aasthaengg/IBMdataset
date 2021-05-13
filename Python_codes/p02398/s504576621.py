a=[]
A,B,C= map(int, input().split())       
for x in range(A,B+1):
    if C%x==0:
        a.append(x)
    else:
        pass
y =len(a)
print(y)