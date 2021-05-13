n,k = map(int,input().split())
p = pow(10,9)+7
li = [1]*(n+2)

counter = 0
k = min(k,n-1)

for a in range(1,n+1):
    li[a] = a*li[a-1]%p

def comb(a,b):
    if b<1:
        return 1
    return li[a]*pow(li[b],p-2,p)*pow(li[a-b],p-2,p)


for i in range(k+1):
    counter += comb(n,i)*comb(n-1,i)%p
    #nCi*  (n-1)Cn-i-1


    #n人をn-iのぐるーぷに分ける

print(counter%p)