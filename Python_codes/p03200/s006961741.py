s=input()
check=list(s)
n=len(s)
cntb=0
for i in check:
    if i=='B':
        cntb+=1
minus=sum([i+1 for i in range(n) if check[i]=='B' ])
plus=sum(range(n-cntb+1,n+1))
print(plus-minus)