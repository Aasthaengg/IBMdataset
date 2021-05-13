N=int(input())
print(0)
S0 = input()[0]
if S0=="V":exit()
print(N-1)
if input()[0]=="V":exit()

l,r=0,N-1
while r-l>1:
    med=(r+l)//2
    print(med)
    S1=input()[0]
    if S1=="V":
        exit()
    elif (med%2==0 and S1==S0) or (med%2==1 and S1!=S0):
        l=med
    else:
        r=med
print(r)
