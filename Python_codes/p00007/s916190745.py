n=input()
loan=10**5
for i in xrange(n):
    loan+=loan*0.05
    if loan%1000!=0:
        loan-=loan%1000
        loan+=10**3
    else:
        loan-=loan%1000
print(int(loan))