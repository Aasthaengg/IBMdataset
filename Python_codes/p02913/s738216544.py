N=int(input())
S=input()

l,r=0,1
res=0
def check(l,r):
    #半閉区間[l,r)
    if not l<r:
        return False
    t=S[l:r]
    s=S[r:]
    n=(r-l)
    for i in range(len(s)-n+1):
        if s[i:i+n]==t:
            return True
    return False
        


while l<N and r<N:
    if r==l:
        r+=1
    if check(l,r):
        res=max(r-l,res)
        r+=1
    else:
        l+=1
    
print(res)