n,k = map(int,input().split())

#コイン投げの回数
def coincnt(base,k):
    ans = 0
    while base<k:
        ans+=1
        base*=2
        
    return ans

p=0.0
for i in range(1,n+1):
    p+=(1/n)*(1/2)**coincnt(i,k)
    
print(p)