import itertools
n=int(input())
p=list(map(int,input().split()))

q=list(map(int,input().split()))
g=list(itertools.permutations([i for i in range(1,n+1)]))

kai=1

for i in range(n):
    kai*=i+1

for i in range(kai):
    if all(p[w]==g[i][w] for w in range(n)):
        a=i+1
for i in range(kai):
    if all(q[w]==g[i][w] for w in range(n)):
        b=i+1
print(abs(a-b))


    
        
        
    
    
    
    
        
