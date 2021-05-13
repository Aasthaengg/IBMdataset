s=input()
n=len(s)-1

res=0
if n==0:
    res=int(s)
    
for i in range(2**n):
    B=format(i,'b').zfill(n)+'1'
    left=0
    for j in range(n+1):
        if B[j]=='1':
            res+=int(s[left:j+1])
            left=j+1
        
print(res)

