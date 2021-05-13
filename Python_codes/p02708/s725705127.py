nk=input("").split(" ")
n=int(nk[0])
k=int(nk[1])
s=0
for i in range(k,n+2):
    s+=(n-i+1)*i+1
print(int(s%(10**9+7)))
    
