A,B,K=map(int,input().split())
if A>=B:
    A^=B
    B^=A
    A^=B
a=[]
for i in range(1,A+1):
    if A%i==0 and B%i==0:
        a.append(i)
print(a[-K])
